from rest_framework import viewsets, generics
from .models import Post
from .serializers import PostSerializer

# class PostList(generics.ListAPIView):
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer