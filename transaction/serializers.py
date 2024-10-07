# blog/serializers.py
from rest_framework import serializers
from .models import Transaction
from content.serializers import ContentSerializer

class ListTransactionSerializer(serializers.ModelSerializer):
    content = ContentSerializer()
    class Meta:
        model = Transaction
        fields = ['name','email','donation_nominal','content','message']  # Atau kamu bisa menentukan field tertentu

  
class CreateTransactionSerializer(serializers.ModelSerializer):
    email = serializers.EmailField() 
    class Meta:
        model = Transaction
        fields = ['name','email','donation_nominal','content','message']  # Atau kamu bisa menentukan field tertentu
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    # def validate_email(self, value):
    #     if not value:
    #         raise serializers.ValidationError("Field is required.")
    #     return value
    
    def validate_message(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    def validate_donation_nominal(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
  
