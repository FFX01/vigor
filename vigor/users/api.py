from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.contrib.auth import get_user_model


class UserResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'height': 'height',
        'weight': 'weight'
    })

    def list(self):
        return get_user_model().objects.all()

    def detail(self, pk):
        return get_user_model().objects.get(id=pk)
