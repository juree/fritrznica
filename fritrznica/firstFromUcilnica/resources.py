from tastypie.resources import ModelResource
from data.models import Offers

class OffersResource(ModelResource):
    class Meta:
        queryset = Offers.objects.all()
        resource_name = 'offers'
        allowed_methods = ['get']
        filtering = {
            "version" : 'exact',
        }
