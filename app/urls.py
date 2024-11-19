from django.contrib import admin
from django.urls import path
# from genres.views import genre_create_list_view, genre_detail_update_view
from genres.views import GenreListCreateView, GenreRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreListCreateView.as_view(), name="genre-list-create"),
    path('genres/<int:id>', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-update'),
    path('actors/', ActorCreateListView.as_view(), name="actor-list-create"),
    path('actors/<int:id>', ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-update'),
    path('movies/', MovieCreateListView.as_view(), name="movie-list-create"),
    path('movies/<int:id>', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail-update'),
]
