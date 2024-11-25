from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.ReviewCreateListView.as_view(), name="review-list-create"),
    path('reviews/<int:id>', views.ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail-update'),   
]

