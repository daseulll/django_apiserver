from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.decorators import list_route, detail_route
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    # /sample_3/post/ => list() 호출
    # /sample_3/post/public_list/ => public_list() 호출
    @list_route()
    def public_list(self, request):
        qs = self.queryset.filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    # /sample_3/post/10 => retrieve() 호출
    # /sample_3/post/10/set_public => set_public() 호출
    @detail_route(methods=['patch'])
    # method를 지정해주면 해당 요청방식으로 전달받는다.
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)