from restless.preparers import FieldsPreparer
from api.resources import PaginatedDjangoResource

from django.contrib.auth import get_user_model


class UserResource(PaginatedDjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'username': 'username',
        'height': 'height',
        'weight': 'weight',
    })
    model = get_user_model()
    allowed_filters = {
        'height': ('gt', 'gte', 'lte', 'exact'),
        'weight': ('gt', 'gte', 'lte', 'exact')
    }

    def is_authenticated(self):
        if self.endpoint in ('update', 'delete'):
            return self.request.user.is_authenticated()
        return True

    def create(self):
        obj = self.model.objects.create_user(
            username=self.data.get("username"),
            password=self.data.get("password"),
            email=self.data.get("email"),
            height=self.data.get("height", 0),
            weight=self.data.get("weight", 0)
        )
        return obj

    def list(self, *args, **kwargs):
        return self.get_obj_list()

    def detail(self, pk):
        return self.get_obj(pk)

    def update(self, pk, **kwargs):
        obj = self.get_obj(pk)
        for key, value in self.data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        obj.save()
        return obj

    def delete(self, pk, **kwargs):
        obj = self.get_obj(pk)
        obj.delete()
        return None
