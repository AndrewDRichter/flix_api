from django.urls import path
from . import views


urlpatterns = [
    path('movies/', views.MovieCreateListView.as_view(), name="movie-list-create"),
    path('movies/<int:id>', views.MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-update'),
    path('movies/stats/', views.MovieStatsView.as_view(), name='movie-stats'),
]