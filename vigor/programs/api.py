from restup import ModelResource
from .models import Program, Period, Session, Exercise


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
        'styles': {
            'attribute': 'styles'
        },
        'maintainers': {
            'attribute': 'maintainers'
        },
        'followers': {
            'attribute': 'followers'
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


class PeriodResource(ModelResource):

    model = Period

    schema = {
        'id': {
            'attribute': 'id',
            'writeable': False
        },
        'number': {
            'attribute': 'number'
        },
        'description': {
            'attribute': 'description'
        },
        'program': {
            'attribute': 'program'
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


class SessionResource(ModelResource):

    model = Session

    schema = {
        'id': {
            'attribute': 'id',
            'writeable': False
        },
        'number': {
            'attribute': 'number'
        },
        'description': {
            'attribute': 'description'
        },
        'period': {
            'attribute': 'period'
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


class ExerciseResource(ModelResource):

    model = Exercise

    schema = {
        'id': {
            'attribute': 'id',
            'writeable': False
        },
        'name': {
            'attribute': 'name'
        },
        'session': {
            'attribute': 'session'
        },
        'styles': {
            'attribute': 'styles'
        },
        'order': {
            'attribute': 'order'
        },
        'sets': {
            'attribute': 'sets'
        },
        'weight': {
            'attribute': 'weight'
        },
        'duration': {
            'attribute': 'duration'
        },
        'notes': {
            'attribute': 'notes'
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
