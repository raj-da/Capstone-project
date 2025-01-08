from rest_framework import serializers
from recipes import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username')


class RecpieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Recipe
        fields = '__all__'


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'