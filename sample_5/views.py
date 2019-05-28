from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorUpdateOrReadonly

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorUpdateOrReadonly]

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            ip=self.request.META['REMOTE_ADDR']
            )
            