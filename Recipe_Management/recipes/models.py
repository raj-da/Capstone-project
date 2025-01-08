from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# recipe catagory model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

# recipe model
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    ingredient = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    catagory_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='recipes', blank=True)

    def __str__(self):
        return self.title
