from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

post_list = PostViewSet.as_view({
    'get' : 'list',
})
# post_list 뷰 함수를 생성

post_detail = PostViewSet.as_view({
    'get' : 'retrieve',
})

