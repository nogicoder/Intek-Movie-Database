from django.urls import path
from .views import (MovieListView, MovieDetailView, MovieCreateView,
                    MovieUpdateView, MovieDeleteView, ActorListView, ActorDetailView,
                    ActorUpdateView, ActorCreateView, ActorDeleteView, AwardListView, AwardDetailView,
                    AwardUpdateView, AwardCreateView, AwardDeleteView, add_mvcomment, del_mvcomment,
                    edit_mvcomment, add_accomment, del_accomment, edit_accomment, add_awcomment,
                    del_awcomment, edit_awcomment)

# Set up the app name in the namespace
app_name = 'core'

# Defining url paths that map to the Views
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movielist'),
    path('movies/create/', MovieCreateView.as_view(), name='moviecreate'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='moviedetail'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movieupdate'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='moviedelete'),
    path('movies/<int:pk>/add_comment/', add_mvcomment, name='addmvcomment'),
    path('movies/<int:pk>/delete_comment/',
         del_mvcomment, name='delmvcomment'),
    path('movies/<int:pk>/edit_comment/', edit_mvcomment, name='editmvcomment'),
    path('actors/', ActorListView.as_view(), name="actorlist"),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name="actordetail"),
    path('actors/create/', ActorCreateView.as_view(), name='actorcreate'),
    path('actors/<int:pk>/update/', ActorUpdateView.as_view(), name='actorupdate'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='actordelete'),
    path('actors/<int:pk>/add_comment/', add_accomment, name='addaccomment'),
    path('actors/<int:pk>/delete_comment/',
         del_accomment, name='delaccomment'),
    path('actors/<int:pk>/edit_comment/', edit_accomment, name='editaccomment'),
    path('awards/', AwardListView.as_view(), name="awardlist"),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name="awarddetail"),
    path('awards/create/', AwardCreateView.as_view(), name='awardcreate'),
    path('awards/<int:pk>/update/', AwardUpdateView.as_view(), name='awardupdate'),
    path('awards/<int:pk>/delete/', AwardDeleteView.as_view(), name='awarddelete'),
    path('awards/<int:pk>/add_comment/', add_awcomment, name='addawcomment'),
    path('awards/<int:pk>/delete_comment/',
         del_awcomment, name='delawcomment'),
    path('awards/<int:pk>/edit_comment/', edit_awcomment, name='editawcomment'),
]
