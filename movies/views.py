from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from .models import Movie
from .serializers import MovieModelSerializer
from app.permissions import GlobalDefaultPermission

class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    lookup_field = 'id'
    
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    
    def get(self, request):
        return response.Response(
            data={"olá": "mundo"},
            status=status.HTTP_200_OK
        )