from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.CreateRecipe.as_view(), name='create recipe'),
]