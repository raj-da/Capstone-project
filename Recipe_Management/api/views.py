from rest_framework import generics
from recipes import models
from . import serializer

class CreateRecipe(generics.CreateAPIView):
    serializer_class = serializer.RecpieSerializer


class RettriveRecipes(generics.ListAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


class DetailView(generics.RetrieveAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


class UpdateView(generics.RetrieveUpdateAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


class DeleteView(generics.RetrieveDestroyAPIView):
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer

