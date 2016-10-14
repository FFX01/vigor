from restless.dj import DjangoResource
from django.core.paginator import Paginator, InvalidPage


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
