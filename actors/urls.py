from django.urls import path
from . import views


urlpatterns = [
    path('actors/', views.ActorCreateListView.as_view(), name="actor-list-create"),
    path('actors/<int:id>', views.ActorRetrieveUpdateDestroyView.as_view(), name='actor-detail-update'),
]
