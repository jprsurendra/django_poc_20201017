from rest_framework import viewsets
from rest_framework.response import Response

from .models import Authors
from .serializers import AuthorSerializer

class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer

'''
Help Link: https://www.django-rest-framework.org/api-guide/viewsets/
'''
class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Authors.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)
    '''
    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
    '''
