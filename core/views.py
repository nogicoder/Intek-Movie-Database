from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Movie, Actor, Award, MovieComment, ActorComment, AwardComment
from .forms import (MovieForm, ActorForm, AwardForm, MovieCommentForm,
                    ActorCommentForm, AwardCommentForm)


class MovieListView(ListView):
    """
    Views for the movie list
    """

    # Defining model for the Views and Template
    model = Movie
    template_name = 'core/movie_list.html'

    # Parsing form into the context
    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = MovieForm
        return context


class MovieDetailView(DetailView):
    """
    Views for the detail movie.
    """

    model = Movie
    template_name = 'core/movie_detail.html'

    # Parsing form into the context
    def get_context_data(self, object):
        context = super().get_context_data()
        context['form'] = MovieCommentForm
        return context


class MovieCreateView(CreateView):
    """
    Views for adding new movie.
    """

    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movielist')


class MovieUpdateView(UpdateView):
    """
    Views for updating existed movie.
    """

    model = Movie
    form_class = MovieForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:movielist')


class MovieDeleteView(DeleteView):
    """
    Views for deleting existed movie.
    """

    model = Movie
    success_url = reverse_lazy('core:movielist')


def add_mvcomment(request, pk):
    """
    Views for adding new comments.
    """

    # Getting the movie object hosting the comment
    movie = get_object_or_404(Movie, pk=pk)

    # if POST
    if request.method == "POST":
        form = MovieCommentForm(request.POST)

        # set the author and redirect if valid form
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.movie = movie
            comment.save()
            return redirect('../', pk=movie.pk)
    else:
        form = MovieCommentForm()

    # render the form through the template
    return render(request, {'form': form})


def del_mvcomment(request, pk):
    """
    Views for deleting new comments.
    """

    comment = get_object_or_404(MovieComment, pk=pk)
    comment.delete()
    movie = comment.movie
    url = '../../' + str(comment.movie.pk)
    return redirect(url)


def edit_mvcomment(request, pk):
    """
    Views for editing new comments.
    """

    comment = get_object_or_404(MovieComment, pk=pk)

    if request.method == "POST":
        form = MovieCommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            url = '../../' + str(comment.movie.pk)
            return redirect(url)
    else:
        form = MovieCommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, context)


class ActorListView(ListView):
    """
    Views for Actor List.
    """

    model = Actor
    template_name = 'core/actor_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = ActorForm
        return context


class ActorDetailView(DetailView):
    """
    Views for Actor Details.
    """

    model = Actor
    template_name = 'core/actor_detail.html'

    def get_context_data(self, object):
        context = super().get_context_data()
        context['form'] = ActorCommentForm
        return context


class ActorCreateView(CreateView):
    """
    Views for adding new actor.
    """

    model = Actor
    form_class = ActorForm
    success_url = reverse_lazy('core:actorlist')


class ActorUpdateView(UpdateView):
    """
    Views for updating existed actor.
    """

    model = Actor
    form_class = ActorForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:actorlist')


class ActorDeleteView(DeleteView):
    """
    Views for deleting existed actor.
    """

    model = Actor
    success_url = reverse_lazy('core:actorlist')


def add_accomment(request, pk):
    """
    Views for adding new comments.
    """

    actor = get_object_or_404(Actor, pk=pk)
    if request.method == "POST":
        form = ActorCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.actor = actor
            comment.save()
            return redirect('../', pk=actor.pk)
    else:
        form = ActorCommentForm()
    return render(request, {'form': form})


def del_accomment(request, pk):
    """
    Views for deleting comments.
    """

    comment = get_object_or_404(ActorComment, pk=pk)
    comment.delete()
    actor = comment.actor
    url = '../../' + str(comment.actor.pk)
    return redirect(url)


def edit_accomment(request, pk):
    """
    Views for updating comments.
    """

    comment = get_object_or_404(ActorComment, pk=pk)
    form = ActorCommentForm()
    if request.method == "POST":
        form = ActorCommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            url = '../../' + str(comment.actor.pk)
            return redirect(url)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, context)


class AwardListView(ListView):
    """
    Views for Award List.
    """

    model = Award
    template_name = 'core/award_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['form'] = AwardForm
        return context


class AwardDetailView(DetailView):
    """
    Views for Award Detail.
    """

    model = Award
    template_name = 'core/award_detail.html'

    def get_context_data(self, object):
        context = super().get_context_data()
        context['form'] = AwardCommentForm
        return context


class AwardCreateView(CreateView):
    """
    Views for creating new Award.
    """

    model = Award
    form_class = AwardForm
    success_url = reverse_lazy('core:awardlist')


class AwardUpdateView(UpdateView):
    """
    Views for updating award.
    """

    model = Award
    form_class = AwardForm
    template_name_suffix = '_update'
    success_url = reverse_lazy('core:awardlist')


class AwardDeleteView(DeleteView):
    """
    Views for deleting award.
    """

    model = Award
    success_url = reverse_lazy('core:awardlist')


def add_awcomment(request, pk):
    """
    Views for adding new comment.
    """

    award = get_object_or_404(Award, pk=pk)
    if request.method == "POST":
        form = AwardCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.award = award
            comment.save()
            return redirect('../', pk=award.pk)
    else:
        form = AwardCommentForm()
    return render(request, {'form': form})


def del_awcomment(request, pk):
    """
    Views for deleting comment.
    """
    comment = get_object_or_404(AwardComment, pk=pk)
    comment.delete()
    award = comment.award
    url = '../../' + str(comment.award.pk)
    return redirect(url)


def edit_awcomment(request, pk):
    """
    Views for editing comment.
    """
    comment = get_object_or_404(AwardComment, pk=pk)

    if request.method == "POST":
        form = AwardCommentForm(request.POST, instance=comment)

        if form.is_valid():
            form.save()
            url = '../../' + str(comment.award.pk)
            return redirect(url)
    else:
        form = AwardCommentForm(instance=comment)

    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, context)
