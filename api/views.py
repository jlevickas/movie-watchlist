from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/movies/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of movies'
        },
        {
            'Endpoint': '/movies/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single movie'
        },
        {
            'Endpoint': '/movies/add/',
            'method': 'POST',
            'body': {'name': "", 'note': ""},
            'description': 'Adds new movie with data sent in post request'
        },
        {
            'Endpoint': '/movies/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting movie'
        },
    ]
    return Response(routes)


@api_view(['GET', 'POST'])
def movieList(request):

    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-created')
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        movie = Movie.objects.create(
            name=data['name'],
            note=data['note'],
            is_watched=data['is_watched']
        )
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def movie(request, id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        movie = Movie.objects.get(id=id)
        data = request.data
        serializer = MovieSerializer(instance=movie, data=data, many=False)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return Response("Movie removed from list")
