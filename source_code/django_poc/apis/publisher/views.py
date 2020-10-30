from rest_framework import viewsets
from .models import Publisher
from .serializers import PublisherSerializer, PublisherNameSerializer
from rest_framework import permissions, generics

class PublisherModelViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublishersList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherNameSerializer
