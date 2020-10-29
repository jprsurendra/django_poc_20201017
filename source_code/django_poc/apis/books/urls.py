from django.conf.urls import url
from rest_framework import routers

from apis.books.views import BooksModelViewSet

router = routers.DefaultRouter()
router.register(r'common_operations', BooksModelViewSet)

# urlpatterns = [
# ]
urlpatterns = router.urls

app_name = 'books'