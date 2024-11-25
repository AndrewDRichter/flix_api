from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.GenreListCreateView.as_view(), name="genre-list-create"),
    path('genres/<int:id>', views.GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-update'),
]
