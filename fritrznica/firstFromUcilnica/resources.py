from tastypie.resources import ModelResource
from data.models import Offers
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):

    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']

class OffersResource(ModelResource):

    user = fields.ForeignKey(UserResource, 'user')

    def build_filters(self, filters=None):
        if not filters:
            return filters

        applicable_filters = {}
        # Normal filtering
        filter_params = dict([(x, filters[x]) for x in filter(lambda x: not x.startswith('!'), filters)])
        applicable_filters['filter'] = super(OffersResource, self).build_filters(filter_params)
        # Exclude filtering
        exclude_params =  dict([(x[1:], filters[x]) for x in filter(lambda x: x.startswith('!'), filters)])
        applicable_filters['exclude'] = super(OffersResource, self).build_filters(exclude_params)

        return applicable_filters

    def apply_filters(self, request, applicable_filters):
        objects = self.get_object_list(request)

        f = applicable_filters.get('filter')
        if f:
            objects = objects.filter(**f)
        e = applicable_filters.get('exclude')
        if e:
            objects = objects.exclude(**e)
        return objects

    class Meta:
        queryset = Offers.objects.all()
        resource_name = 'offers'
        allowed_methods = ['get']
        filtering = {
            "user" : 'exact',
            "version" : 'exact',
            "offered" : 'exact',
            "closed" : 'exact',
        }
