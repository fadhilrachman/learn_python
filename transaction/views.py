from rest_framework import generics
from .models import Transaction
from .serializers import ListTransactionSerializer, CreateTransactionSerializer
from .pagination import CustomPageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated  

class TransactionListForAdmin(generics.ListAPIView):
    permission_classes = [IsAuthenticated] 
    queryset = Transaction.objects.select_related('content').all()
    serializer_class = ListTransactionSerializer
    pagination_class = CustomPageNumberPagination 
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['content']
    
    
class TransactionCreateForUser(APIView):
    @swagger_auto_schema(
        request_body=CreateTransactionSerializer,
        responses={201: CreateTransactionSerializer}
    )
    def post(self,request):
        serializer = CreateTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)
   

