from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register user'),
    path('create/', views.CreateRecipe.as_view(), name='create recipe'),
    path('retrieve/', views.RettriveRecipes.as_view(), name='retrieve recipes'),
    path('retrieve/<int:pk>/', views.DetailView.as_view(), name='Detail view'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update view'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete view'),
]