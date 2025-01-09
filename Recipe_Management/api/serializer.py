from rest_framework import serializers
from recipes import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'] # here the password is hashed before it is saved
        )   
        return user



class RecpieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = '__all__'


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'