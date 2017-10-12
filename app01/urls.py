'''
from django.conf.urls import patterns, include, url
from durationfield.db.models.fields.duration import DurationField
from app01 import models
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

'''
'''
class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Test
        fields = ('url', 'username', 'password')

# ViewSets define the view behavior.
class TestViewSet(viewsets.ModelViewSet):
    queryset = models.Test.objects.all()
    serializer_class = TestSerializer
'''
'''

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'test', TestViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_08bbs.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
'''