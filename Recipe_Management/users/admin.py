from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()

# add custom user to the admin pannal
admin.site.register(user)
