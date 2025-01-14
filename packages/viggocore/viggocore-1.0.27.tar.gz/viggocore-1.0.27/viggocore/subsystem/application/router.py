from viggocore.common.subsystem import router


class Router(router.Router):

    def __init__(self, collection, routes=[]):
        super().__init__(collection, routes)

    @property
    def routes(self):
        settings_endpoint = '/settings'
        return super().routes + [
            {
                'action': 'getApplicationRoles',
                'method': 'GET',
                'url': self.resource_url + '/roles',
                'callback': 'get_roles'
            },
            {
                'action': 'Update settings on Application',
                'method': 'PUT',
                'url': self.resource_url + settings_endpoint,
                'callback': 'update_settings',
                'bypass': False
            },
            {
                'action': 'Remove settings from Application',
                'method': 'DELETE',
                'url': self.resource_url + settings_endpoint,
                'callback': 'remove_settings',
                'bypass': False
            },
            {
                'action': 'Get settings by keys from Application',
                'method': 'GET',
                'url': self.resource_url + settings_endpoint,
                'callback': 'get_application_settings_by_keys',
                'bypass': False
            }
        ]
