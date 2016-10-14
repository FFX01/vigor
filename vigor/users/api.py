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
            return self.request.user.is_authenticateed()
        return True

    def create(self):
        return self.model.objects.create_user(
            username=self.data.get("username"),
            password=self.data.get("password"),
            email=self.data.get("email"),
            height=self.data.get("height", 0),
            weight=self.data.get("weight", 0)
        )

    def list(self, *args, **kwargs):
        results = self.apply_filters(
            self.model.objects.all()
        )
        return self.paginate_objects(results)

    def detail(self, pk):
        return self.model.objects.get(id=pk)
