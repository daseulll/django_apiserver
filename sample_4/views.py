from sample_3.models import Post
from sample_3.serializers import PostSerializer
from rest_framework.viewsets import ModelViewSet

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()  # empty result
        return qs
            