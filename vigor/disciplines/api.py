from api.resources import PaginatedDjangoResource
from restless.preparers import FieldsPreparer
from django.contrib.auth import get_user_model

from .models import Discipline, DisciplinePractice


class DisciplineResource(PaginatedDjangoResource):

    preparer = FieldsPreparer(fields={
        "id": "id",
        "name": "name",
        "description": "description",
        "creator": "creator.pk",
        "practitioners": "_meta.get_field('practitioners')",
        "created": "created",
        "updated": "updated"
    })
    model = Discipline
    allowed_filters = {
        "creator": ("exact", )
    }

    def is_authenticated(self):
        if self.endpoint in ("create", "update", "delete"):
            return self.request.user.is_authenticated()
        else:
            return True

    def create(self):
        obj = self.model.objects.create(
            name=self.data.get("name"),
            description=self.data.get("description"),
            creator=get_user_model().objects.get(
                id=self.data.get("creator")
            ),
        )
        return obj

    def list(self):
        return self.get_obj_list()

    def detail(self, pk):
        return self.get_obj(pk)

    def update(self, pk):
        obj = self.get_obj(pk)
        for key, value in self.data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
        return obj

    def delete(self, pk):
        obj = self.get_obj()
        obj.delete()
        return None


class DisciplinePracticeResource(PaginatedDjangoResource):

    model = DisciplinePractice

    preparer = FieldsPreparer(fields={
        "user": "user",
        "discipline": "discipline",
        "started": "started",
        "is_current": "is_current",
        "ended": "ended",
        "notes": "notes"
    })

    def list(self):
        return self.model.objects.all()

    def detail(self, pk):
        return self.model.objects.get(id=pk)
