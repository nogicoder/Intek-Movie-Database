# users/views.py
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('core:MovieList')
    template_name = 'users/signup.html'


class HomePageView(TemplateView):
    template_name = 'home.html'