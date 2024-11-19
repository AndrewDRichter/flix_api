# import json
# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import Genre
from .serializers import GenreSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# @csrf_exempt
# def genre_create_list_view(request):
#     if request.method == 'GET':
#         genres = Genre.objects.all()
#         data = [{'id': genre.id, 'name': genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)
#     elif request.method == 'POST':
#         data = json.loads(request.body.decode('utf-8'))
#         new_genre = Genre(name=data['name'])
#         new_genre.save()
#         return JsonResponse(
#             {'id': new_genre.id, 'name': new_genre.name},
#             status=201,
#         )


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'id'

# @csrf_exempt 
# def genre_detail_update_view(request, id):
#     genre = get_object_or_404(Genre, id=id)

#     if request.method == 'GET':
#         data = {'id': genre.id, 'name': genre.name}

#     elif request.method == "PUT":
#         payload = json.loads(request.body.decode('utf-8'))
#         if payload['name']:
#             genre.name = data['name']
#             genre.save()
#             data = {'id': genre.id, 'name': genre.name}
#         else:
#             data = {'error': 'not a valid parameter'}

#     elif request.method == "DELETE":
#         genre.delete()
#         return JsonResponse({"message": "genre deleted successful"}, status=204,)

#     return JsonResponse(data)
