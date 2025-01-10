from rest_framework import generics
from recipes import models
from . import serializer
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAuthenticated


# custom persmission calss
class UpdateDeletePermission(BasePermission):
    message = 'Editing or deleting Posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return obj.user_id == request.user


# api view to register a user
class RegisterUser(generics.CreateAPIView):
    serializer_class = serializer.UserSerializer


# api view to create a recipe
class CreateRecipe(generics.CreateAPIView):
    serializer_class = serializer.RecpieSerializer


# api view to retrive all recipes
class RettriveRecipes(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


# api view to see detail of a post
class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


# api view to update a recipe
class UpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [UpdateDeletePermission, IsAuthenticated]
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer


# api view to delete a post
class DeleteView(generics.RetrieveDestroyAPIView):
    permission_classes = [UpdateDeletePermission, IsAuthenticated]
    queryset = models.Recipe.objects.all()
    serializer_class = serializer.RecpieSerializer

