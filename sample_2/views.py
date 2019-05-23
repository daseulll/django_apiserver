from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer, UserSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class PostListAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# user_list = UserViewSet.as_view({
#     'get' : 'list', # 호출될 함수와 호출할 함수를 지정
# })

# user_detail = UserViewSet.as_view({
#     'get' : 'retrieve',
# })
### router사용시 이 코드는 필요없어 진다.
