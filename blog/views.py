from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny 

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated] 
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination 
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListForUser(generics.ListAPIView):
    permission_classes = [AllowAny] 

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination 