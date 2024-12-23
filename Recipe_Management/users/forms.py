from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

user = get_user_model()

class NewUserCreationForm(UserCreationForm):
    class Meta:
        model = user
        fields = ('username', 'email', 'password1', 'password2')