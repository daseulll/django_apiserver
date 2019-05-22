from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, 
                    generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        # *args, **kwargs는 가변인자로서, 넘어오는 갯수 상관없이 다 받아들이겠다는 뜻
        return self.list(request)

    def post(self, request, *args, **kwargs):
        return self.create(request)

# class PostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.all()
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PostSerializer(data=request.POST)
#         if serializer.is_valid():
#             serializer.save()
#             # 직렬화할 data가 serializer.data에 저장
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# /post/10/ => GET, PUT, DELETE

class PostDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class PostDetailAPIView(APIView):
#     def get_object(self, pk):
#         return get_object_or_404(Post, pk=pk)
        
#     def get(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         print(post)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         # serializer의 인자는 (instance, data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serialzer.errors, status=400)

#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=204)