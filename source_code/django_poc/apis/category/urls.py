from django.conf.urls import url
from rest_framework import routers

from apis.category.views import CategoryModelViewSet

router = routers.DefaultRouter()
router.register(r'common_operations', CategoryModelViewSet)

urlpatterns = router.urls
app_name = 'category'