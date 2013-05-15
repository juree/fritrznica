from tastypie.resources import ModelResource
from data.models import Parsedoffers
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie import fields
from django.contrib.auth.models import User

class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'user'
    fields = ['username', 'first_name', 'last_name']
    allowed_methods = ['get']
    filtering = {
      'username': ALL,
      'id': ALL,
    }

class ParsedoffersResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = Parsedoffers.objects.all()
        resource_name = 'parsedoffers'
        allowed_methods = ['get']
        filtering = {
            "user" : ALL_WITH_RELATIONS,
            "offered" : 'exact',
            "version" : 'exact',
        }