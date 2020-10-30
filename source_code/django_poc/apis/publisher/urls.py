from django.conf.urls import url
from rest_framework import routers

from apis.publisher.views import  PublisherModelViewSet, PublishersList

router = routers.DefaultRouter()
router.register(r'common_operations', PublisherModelViewSet)

urlpatterns = [
    url(r'^publisher-name-list/$', PublishersList.as_view(), name='publisher-name-list'),
]
urlpatterns += router.urls
app_name = 'Publisher'

