from django.contrib import admin
from .models import Category

# Registering Category for editing in Admin Interface
admin.site.register(Category)