from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from sample_3.models import Post
from sample_3.serializers import PostSerializer
from .pagination import PostPageNumberPagination

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def get_queryset(self):
        qs = super().get_queryset()

        # search = self.request.GET.get('search', '')
        # qs = qs.filter(title__icontains=search)

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)
        else:
            qs = qs.none()  # empty result
        return qs
            