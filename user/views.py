from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView


class RegisterView(CreateView):
    """
    Views for Registering new user
    """

    # Define template name and form to be used
    template_name = "user/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("user:login")


class HomeView(TemplateView):
    """
    Views for showing the Homepage
    """
    
    template_name = "user/home.html"
