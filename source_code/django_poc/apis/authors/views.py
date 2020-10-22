from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, generics


from .models import Authors
from .serializers import AuthorSerializer, AuthorNameSerializer
from ..common.views import GenericDataWrapper


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all() # SELECT * FROM tbl_authors
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




class AuthorView(GenericDataWrapper, generics.RetrieveUpdateDestroyAPIView):
    model = Authors
    queryset = Authors.objects.all()
    serializer_class = AuthorSerializer
    # lookup_field = 'pk'

    # def get(self, request, *args, **kwargs):
    #     return self.retrieve(request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)

    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)

class AuthorList(generics.ListCreateAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorNameSerializer


