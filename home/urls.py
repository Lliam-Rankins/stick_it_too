from django.urls import path

from . import views

urlpatterns = [
    path('', view=views.HomeView.as_view(), name="home"),
    path('login', view=views.LoginInterfaceView.as_view(), name="login"),
    path('signup', view=views.SignupView.as_view(), name="signup"),
]