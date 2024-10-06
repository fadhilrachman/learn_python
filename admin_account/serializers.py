# admin_account/serializers.py
from rest_framework import serializers
from .models import AdminAccount

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAccount
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = AdminAccount(**validated_data)
        user.set_password(validated_data['password'])  # Enkripsi password
        user.save()
        return user
