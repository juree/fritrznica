from tastypie.resources import ModelResource
from data.models import Swaps


class SwapsResource(ModelResource):
    class Meta:
        queryset = Swaps.objects.all()
        resource_name = 'swaps'
        allowed_methods = ['get']
        filtering = {
            "parsedofferid": 'exact',
        }
