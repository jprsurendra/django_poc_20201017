from django.conf.urls import url
from rest_framework import routers

from apis.authors.views import AuthorModelViewSet, AuthorList

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelViewSet)

urlpatterns = [
    # url(r'^$', AuthorViewSet.as_view({'get': 'list'}), name='author'),
    url(r'^author-name-list/$', AuthorList.as_view(), name='book-author-name-list'),

]
urlpatterns += router.urls

app_name = 'books'