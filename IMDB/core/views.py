from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Movie


class MovieListView(ListView):
    model = Movie
    template_name='core/movie_list.html'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'core/movie_detail.html'


class MovieCreateView(CreateView):
    model = Movie
    fields = "__all__"
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:movielist')


class MovieUpdateView(UpdateView):
    model = Movie
    fields = "__all__"
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:movielist')


class MovieDeleteView(DeleteView):
    model = Movie
    success_url = reverse_lazy('core:movielist')

