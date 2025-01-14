"""Access_key types file."""

import datetime
from pyramid.security import (
    Allow,
    Deny,
    Authenticated,
    Everyone,
)
from pyramid.settings import asbool
from pyramid.view import view_config
from .. import (
    collection,
    load_schema,
)
from ..authentication import (
    generate_password,
    generate_user,
    CRYPT_CONTEXT,
)
from ..crud_views import (
    collection_add,
    item_edit,
)
from ..project_app import app_project
from ..validators import (
    validate_item_content_post,
)
from ..util import debug_log
from .base import (
    Item,
    DELETED_ACL,
    ONLY_ADMIN_VIEW_ACL,
)


@collection(
    name='access-keys',
    properties={
        'title': 'Access keys',
        'description': 'Programmatic access keys',
    },
    acl=[
        (Allow, Authenticated, 'add'),
        (Allow, 'group.admin', 'list'),
        (Allow, 'group.read-only-admin', 'list'),
        (Allow, 'remoteuser.INDEXER', 'list'),
        (Allow, 'remoteuser.EMBED', 'list'),
        (Deny, Everyone, 'list'),
    ])
class AccessKey(Item):
    """AccessKey class."""
    ACCESS_KEY_EXPIRATION_TIME = 90  # days
    item_type = 'access_key'
    schema = load_schema('snovault:schemas/access_key.json')
    embedded_list = []

    STATUS_ACL = {
        'current': [(Allow, 'role.owner', ['view', 'edit'])] + ONLY_ADMIN_VIEW_ACL,
        'deleted': DELETED_ACL,
    }

    @classmethod
    def create(cls, registry, uuid, properties, sheets=None):
        """ Sets the access key timeout 90 days from creation. """
        if app_project().access_key_has_expiration_date():
            properties['expiration_date'] = (datetime.datetime.utcnow() + datetime.timedelta(
                days=cls.ACCESS_KEY_EXPIRATION_TIME)).isoformat()
        return super().create(registry, uuid, properties, sheets)

    def __ac_local_roles__(self):
        """grab and return user as owner."""
        owner = 'userid.%s' % self.properties['user']
        return {owner: 'role.owner'}

    def __json__(self, request):
        """delete the secret access key has from the object when used."""
        properties = super(AccessKey, self).__json__(request)
        del properties['secret_access_key_hash']
        return properties

    def update(self, properties, sheets=None):
        """smth."""
        # make sure PUTs preserve the secret access key hash
        if 'secret_access_key_hash' not in properties:
            new_properties = self.properties.copy()
            new_properties.update(properties)
            properties = new_properties
        # set new expiration
        properties['expiration_date'] = (datetime.datetime.utcnow() + datetime.timedelta(
            days=self.ACCESS_KEY_EXPIRATION_TIME)).isoformat()
        self._update(properties, sheets)

    class Collection(Item.Collection):
        pass


# access keys have view permissions for update so readonly admin and the like
# can create access keys to download files.
@view_config(context=AccessKey.Collection, request_method='POST',
             permission='add',
             validators=[validate_item_content_post])
@debug_log
def access_key_add(context, request):
    """smth."""
    crypt_context = request.registry[CRYPT_CONTEXT]

    if 'access_key_id' not in request.validated:
        request.validated['access_key_id'] = generate_user()

    if 'user' not in request.validated:
        request.validated['user'], = [
            principal.split('.', 1)[1]
            for principal in request.effective_principals
            if principal.startswith('userid.')
        ]

    password = None
    if 'secret_access_key_hash' not in request.validated:
        password = generate_password()
        request.validated['secret_access_key_hash'] = crypt_context.hash(password)

    result = collection_add(context, request)

    if password is None:
        result['secret_access_key'] = None
    else:
        result['secret_access_key'] = password

    result['access_key_id'] = request.validated['access_key_id']
    result['description'] = request.validated.get('description', "")
    return result


@view_config(name='reset-secret', context=AccessKey,
             permission='add',
             request_method='POST', subpath_segments=0)
@debug_log
def access_key_reset_secret(context, request):
    """smth."""
    request.validated = context.properties.copy()
    crypt_context = request.registry[CRYPT_CONTEXT]
    password = generate_password()
    new_hash = crypt_context.hash(password)
    request.validated['secret_access_key_hash'] = new_hash
    result = item_edit(context, request, render=False)
    result['access_key_id'] = request.validated['access_key_id']
    result['secret_access_key'] = password
    return result


@view_config(context=AccessKey, permission='view_raw', request_method='GET',
             name='raw')
@debug_log
def access_key_view_raw(context, request):
    """smth."""
    if asbool(request.params.get('upgrade', True)):
        properties = context.upgrade_properties()
    else:
        properties = context.properties.copy()
    del properties['secret_access_key_hash']
    return properties
