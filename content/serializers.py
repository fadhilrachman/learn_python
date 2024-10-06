# blog/serializers.py
from rest_framework import serializers
from .models import Content

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id','title','description','donation_target_nominal','donation_target_date','is_active','img']  # Atau kamu bisa menentukan field tertentu
    
    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    def validate_description(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    def validate_img(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    def validate_donation_target_nominal(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
    
    def validate_is_active(self, value):
        if not value:
            raise serializers.ValidationError("Field is required.")
        return value
