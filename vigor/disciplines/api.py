from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Discipline, DisciplinePractice


class DisciplineResource(DjangoResource):

    preparer = FieldsPreparer(fields={
        "name": "name",
        "description": "description",
        "creator": "creator",
        "practitioners": "practitioners",
        "created": "created",
        "updated": "updated"
    })

    def list(self):
        return Discipline.objects.all()

    def detail(self, pk):
        return Discipline.objects.get(id=pk)
