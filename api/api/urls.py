from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer
 
from django.contrib import admin
 
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
 
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.
    list:
        Return all users, ordered by most recently joined.
    create:
        Create a new user.
    delete:
        Remove an existing user.
    partial_update:
        Update one or more fields on an existing user.
    update:
        Update a user.
    """
 
    queryset = User.objects.all()
    serializer_class = UserSerializer
 
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
 
# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(title='Users API', renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer])
 
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^docs/', schema_view, name="docs"),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]