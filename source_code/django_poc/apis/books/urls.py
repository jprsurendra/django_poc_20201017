from django.conf.urls import url
from rest_framework import routers

from apis.authors.views import AuthorModelViewSet

router = routers.DefaultRouter()
router.register(r'authors', AuthorModelViewSet)

urlpatterns = router.urls

app_name = 'books'