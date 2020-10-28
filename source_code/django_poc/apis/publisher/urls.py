from django.conf.urls import url
from rest_framework import routers

from apis.publisher.views import  PublisherModelViewSet

router = routers.DefaultRouter()
router.register(r'common_operations', PublisherModelViewSet)

urlpatterns = router.urls
app_name = 'Publisher'

