from django.urls import path
from .views import (MovieListView, MovieDetailView, MovieCreateView,
MovieUpdateView, MovieDeleteView, ActorListView, ActorDetailView,
ActorUpdateView, ActorCreateView, ActorDeleteView, AwardListView, AwardDetailView,
AwardUpdateView, AwardCreateView, AwardDeleteView)

app_name = 'core'
urlpatterns = [
    path('', MovieListView.as_view(), name='movielist'),
    path('movies/', MovieListView.as_view(), name='movielist'),
    path('movies/create/', MovieCreateView.as_view(), name='moviecreate'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='moviedetail'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movieupdate'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='moviedelete'),
    path('actors/', ActorListView.as_view(), name="actorlist"),
    path('actors/<int:pk>/', ActorDetailView.as_view(), name="actordetail"),
    path('actors/create/', ActorCreateView.as_view(), name='actorcreate'),
    path('actors/<int:pk>/update/', ActorUpdateView.as_view(), name='actorupdate'),
    path('actors/<int:pk>/delete/', ActorDeleteView.as_view(), name='actordelete'),
    path('awards/', AwardListView.as_view(), name="awardlist"),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name="awarddetail"),
    path('awards/create/', AwardCreateView.as_view(), name='awardcreate'),
    path('awards/<int:pk>/update/', AwardUpdateView.as_view(), name='awardupdate'),
    path('awards/<int:pk>/delete/', AwardDeleteView.as_view(), name='awarddelete'),
]

