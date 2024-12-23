from django.shortcuts import render
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .forms import NewUserCreationForm
from django.urls import reverse_lazy

# for registering user to database
class Register(generic.CreateView):
    form_class = NewUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'


    def form_invalid(self, form):
        print("Form Invalid", form.errors)
        return super().form_invalid(form)
    

# for logging in
class Login(LoginView):
    template_name = 'users/login.html'


# for logging out
class Logout(LogoutView):
    template_name = 'users/logout.html'

# Profile of the logged user
@login_required
def profile(request):
    user = request.user
    context = {'user': user}

    return render(request=request, template_name='users/profile.html', context=context)

