from restup import ModelResource

from .models import Style


class StyleResource(ModelResource):

    model = Style

    schema = {
        'id': {
            'attribute': 'id',
            'writable': False
        },
        'name': {
            'attribute': 'name'
        },
        'description': {
            'attribute': 'description'
        },
        'maintainers': {
            'attribute': 'maintainers'
        },
        'created': {
            'attribute': 'created',
            'writable': False
        },
        'updated': {
            'attribute': 'updated',
            'writable': False
        }
    }

    def can_create(self, request):
        return self.model.can_create(request.user)

    def can_get(self, obj, request):
        return obj.can_read(request.user)

    def can_get_list(self, object_list, request):
        return [
            obj for obj in object_list if obj.can_read(request.user)
        ]

    def can_update(self, obj, request):
        return obj.can_update(request.user)

    def can_delete(self, obj, request):
        return obj.can_delete(request.user)
