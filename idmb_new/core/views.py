from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Movie, Actor, Award


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


class ActorListView(ListView):
    model = Actor
    template_name='core/actor_list.html'


class ActorDetailView(DetailView):
    model = Actor
    template_name='core/actor_detail.html'


class ActorCreateView(CreateView):
    model = Actor
    fields = "__all__"
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:actorlist')


class ActorUpdateView(UpdateView):
    model = Actor
    fields = "__all__"
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:actorlist')


class ActorDeleteView(DeleteView):
    model = Actor
    success_url = reverse_lazy('core:actorlist')


class AwardListView(ListView):
    model = Award
    template_name='core/award_list.html'


class AwardDetailView(DetailView):
    model = Award
    template_name='core/award_detail.html'


class AwardCreateView(CreateView):
    model = Award
    fields = "__all__"
    template_name_suffix = '_create'
    success_url = reverse_lazy('core:awardlist')
    

class AwardUpdateView(UpdateView):
    model = Award
    fields = "__all__"
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:awardlist')


class AwardDeleteView(DeleteView):
    model = Award
    success_url = reverse_lazy('core:awardlist')


