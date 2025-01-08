from rest_framework import generics
from . import serializer

class CreateRecipe(generics.CreateAPIView):
    serializer_class = serializer.RecpieSerializer
