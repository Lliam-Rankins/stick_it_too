from django.shortcuts import render

# Tools
from django.shortcuts import redirect

# Views
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView

# Forms
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'


# Login View
class LoginInterfaceView(LoginView):
    template_name= 'home/login.html'

# Signup View
class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/signup.html'
    success_url = 'board/<ink:pk>'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(request, *args, **kwargs)
    