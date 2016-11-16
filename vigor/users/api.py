from django.contrib.auth import get_user_model

from restup import ModelResource


def is_integer(value):
    return type(value) == int


class UserResource(ModelResource):

    model = get_user_model()

    schema = {
        'id': {
            'attribute': 'id'
        },
        'username': {
            'attribute': 'username'
        },
        'height': {
            'attribute': 'height',
            'filters': (
                'exact', 'gte', 'gt',
                'lte', 'lt'
            ),
            'validators': (
                is_integer,
            )
        },
        'weight': {
            'attribute': 'weight',
            'filters': (
                'exact', 'gte', 'gt',
                'lte', 'lt'
            ),
            'validators': (
                is_integer,
            )
        },
        'date_joined': {
            'attribute': 'date_joined',
            'writeable': False
        },
        'email': {
            'attribute': 'email',
            'readable': True
        },
        'password': {
            'attribute': 'password',
            'readable': False,
        },
        'practiced_disciplines': {
            'attribute': 'practiced_disciplines'
        },
        'created_disciplines': {
            'attribute': 'created_disciplines'
        }
    }
