from django.contrib import admin
from django.urls import path
# from genres.views import genre_create_list_view, genre_detail_update_view
from genres.views import GenreCreateListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name="genre-create-list"),
    # path('genres/<int:id>', genre_detail_update_view, name='genre-detail-update')
]
