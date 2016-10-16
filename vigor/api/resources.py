from restless.dj import DjangoResource
from django.core.paginator import Paginator, InvalidPage
from django.conf.urls import url
from django.http import HttpResponse
from . import exceptions
from .serializers import JsonSerializer


class ModelResource(object):

    SAFE_METHODS = ("GET", )

    ALL_METHODS = ("GET", "POST", "PUT", "DELETE")

    ACTIONS = {
        "list": {
            "GET": "list",
            "POST": "create",
        },
        "detail": {
            "GET": "detail",
            "PUT": "update",
            "DELETE": "delete"
        },
        "list_schema": {
            "GET": "list_schema"
        },
        "detail_schema": {
            "GET": "detail_schema"
        }
    }

    model = None
    per_page = 10
    paginator_class = Paginator
    serializer = JsonSerializer
    filters = {}
    schema = {}
    allowed_methods = ALL_METHODS

    def __init__(self, *args, **kwargs):
        self.init_args = args
        self.init_kwargs = kwargs
        self.request = None
        self.data = None
        self.action = None
        self.status = 200

    @classmethod
    def as_list(cls, *init_args, **init_kwargs):
        return cls.dispatch('list', *init_args, **init_kwargs)

    @classmethod
    def as_detail(cls):

    @classmethod
    def as_list_schema(cls):

    @classmethod
    def as_detail_schema(cls):

    @classmethod
    def dispatch(cls, view_type, *init_args, **init_kwargs):

        def _wrapper(request, *args, **kwargs):
            instance = cls(*init_args, **init_kwargs)
            instance.request = request
            return instance.route(view_type, *args, **kwargs)

    def route(self, action, *args, **kwargs):
        self.action = action
        method = self.request_method()

        if not method in self.ACTIONS.get(action, {}):
            raise exceptions.NotImplemented(
                msg="'{0}' method not implemented for {1} action.".format(
                    method, action
                )
            )

        if not self.is_authenticated():
            raise exceptions.Unauthorized()

        self.data = self.deserialize(method, action, self.request_body())

        view_action = getattr(self, self.ACTIONS[action][method])

    def is_authenticated(self):
        return True

    def deserialize(self, method, action, body):
        if action in ("list", "list_schema"):
            if body:
                return self.serializer.deserialize(body)
            return []
        else:
            if body:
                return self.serializer.deserialize(body)
            return {}

    def request_body(self):
        pass

    def request_method(self):
        return self.request.method.upper()

    def append_urls(self):
        return []

    @classmethod
    def urls(cls, self):
        return self.append_urls() + [
            url(r'^$', cls.as_list(), name='api_list'),
            url(r'^(?P<pk>\d+)/$', cls.as_detail(), name='api_detail'),
            url(r'^schema/$', cls.as_list_schema(), name='api_list_schema'),
            url(r'^(?<pk>\d+)/schema/$', cls.as_detail_schema, name='api_detail_schema')
        ]

    def create(self, *args, **kwargs):
        pass

    def list(self, *args, **kwargs):
        pass

    def detail(self, *args, **kwargs):
        pass

    def update(self, *args, **kwargs):
        pass

    def delete(self, *args, **kwargs):
        pass

    def list_schema(self, *args, **kwargs):
        pass

    def detail_schema(self, *args, **kwargs):
        pass


class PaginatedDjangoResource(DjangoResource):

    model = None
    per_page = 10
    pagination_class = Paginator
    allowed_filters = {}

    def apply_filters(self, queryset):
        filters = self.build_filters()
        objects = queryset.filter(**filters)
        return objects

    def build_filters(self):
        params = self.request.GET
        filters = {}
        for key, value in params.items():
            field = key.split("__")[0]
            if field in self.allowed_filters.keys():
                filters[key] = value
        return filters

    def paginate_objects(self, objects):
        params = self.request.GET
        limit = int(params.get('limit', self.per_page))
        page_num = int(params.get('page', 1))
        paginator = self.pagination_class(
            object_list=objects,
            per_page=limit
        )
        try:
            page = paginator.page(
                number=page_num
            )
        except InvalidPage:
            return self.build_error(InvalidPage)
        return page

    def build_meta_dict(self, page):
        return {
            "count": page.paginator.count,
            "next": page.next_page_number() if page.has_next() else None,
            "previous": page.previous_page_number() if page.has_previous() else None,
            "page": page.number
        }

    def wrap_list_response(self, data):
        return {
            "meta": self.build_meta_dict(data),
            "objects": data.object_list
        }

    def serialize_list(self, data=None):
        if data is None:
            return ''
        wrapped_data = self.wrap_list_response(data)
        wrapped_data["objects"] = [self.prepare(item) for item in wrapped_data.get("objects")]
        return self.serializer.serialize(wrapped_data)

    def get_obj(self, pk):
        try:
            obj = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise exceptions.NotFound()
        return obj

    def get_obj_list(self):
        results = self.apply_filters(
            self.model.objects.all()
        )
        return self.paginate_objects(results)
