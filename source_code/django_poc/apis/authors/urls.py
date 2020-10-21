from django.conf.urls import url
from rest_framework import routers

from apis.authors.views import AuthorViewSet, AuthorModelViewSet

router = routers.DefaultRouter()
router.register(r'common_operations', AuthorModelViewSet)

urlpatterns = [
    url(r'^$', AuthorViewSet.as_view({'get': 'list'}), name='author'),
]
urlpatterns += router.urls


app_name = 'authors'