
from rest_framework import generics, permissions, response, status
from rest_framework.authentication import BasicAuthentication

from .serializers import *
from .permisisions import *



class ArticleCreateView(generics.CreateAPIView):
    serializer_class = ArticleCreateSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleListSerializer
    queryset = Article.objects.filter(public=True)


class ArticlePrivatListView(generics.ListAPIView):
    serializer_class = ArticlePrivatListSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Article.objects.all()


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    authentication_classes = (BasicAuthentication, )
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Article.objects.all()


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return response.Response(data)