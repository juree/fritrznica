from tastypie.resources import ModelResource
from data.models import Parsedoffers

class ParsedoffersResource(ModelResource):
    class Meta:
        queryset = Parsedoffers.objects.all()
        resource_name = 'parsedoffers'
        allowed_methods = ['get']
