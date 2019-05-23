from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import mixins

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
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