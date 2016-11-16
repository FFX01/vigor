from restup import ModelResource
from .models import Program


class ProgramResource(ModelResource):

    model = Program

    schema = {
        'id': {
            'attribute': 'id',
            'writeable': False
        },
        'name': {
            'attribute': 'name'
        },
        'user': {
            'attribute': 'user'
        },
        'exercises': {
            'attribute': 'exercises'
        },
        'start_date': {
            'attribute': 'start_date'
        },
        'end_date': {
            'attribute': 'end_date'
        },
        'is_current': {
            'attribute': 'is_current'
        }
    }
