# users/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import HomePageView
from . import views


app_name = 'users'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
