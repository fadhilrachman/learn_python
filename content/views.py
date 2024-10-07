from rest_framework import generics
from .models import Content
from .serializers import ContentSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  

class ContentListForUser(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = CustomPageNumberPagination 
    
        
class ContentListForAdmin(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated] 
    serializer_class = ContentSerializer
    pagination_class = CustomPageNumberPagination 
    
    
class ContentDetailForAdmin(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    permission_classes = [IsAuthenticated] 
    serializer_class = ContentSerializer

