from django.conf.urls import url
from rest_framework import routers

from apis.authors.views import AuthorViewSet, AuthorModelViewSet, AuthorView, AuthorList

router = routers.DefaultRouter()
router.register(r'common_operations', AuthorModelViewSet)

urlpatterns = [
    url(r'^$', AuthorViewSet.as_view({'get': 'list'}), name='author'),
    url(r'^author-name-by-id/(?P<pk>\d{0,50})/$', AuthorView.as_view(), name='author-name'),
    url(r'^author-name-list/$', AuthorList.as_view(), name='author-name-list'),
]
urlpatterns += router.urls
app_name = 'authors'