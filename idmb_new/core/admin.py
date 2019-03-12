from django.contrib import admin
from .models import Movie, Actor, Award

model_obj = [Movie, Actor, Award]
admin.site.register(model_obj)