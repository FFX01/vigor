from restup import ModelResource

from .models import Style


class StyleResource(ModelResource):

    model = Style

    schema = {
        'id': {
            'attribute': 'id',
            'writable': 'false'
        },
        'name': {
            'attribute': 'name'
        },
        'description': {
            'attribute': 'description'
        },
        'creator': {
            'attribute': 'creator'
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
