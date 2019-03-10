from django.urls import path
from .views import (MovieListView, MovieDetailView, MovieCreateView,
MovieUpdateView, MovieDeleteView)

app_name = 'core'
urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movielist'),
    path('movies/create/', MovieCreateView.as_view(), name='moviecreate'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='moviedetail'),
    path('movies/<int:pk>/update/', MovieUpdateView.as_view(), name='movieupdate'),
    path('movies/<int:pk>/delete/', MovieDeleteView.as_view(), name='moviedelete'),
]

