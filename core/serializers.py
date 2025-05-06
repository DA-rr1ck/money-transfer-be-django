from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Transfer, UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['receiver', 'amount']
