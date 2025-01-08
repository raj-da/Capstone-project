from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
