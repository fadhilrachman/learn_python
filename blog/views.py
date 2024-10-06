from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination 
    
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCount(APIView):
    def get(self,request):
        count = Post.objects.count()
        return Response({'count':count},status=200)