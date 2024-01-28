from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.status import *


@api_view(['GET', 'POST'])
def directors_list_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)


@api_view(['GET', 'PUT', 'DELETE'])
def directors_detail_view(request, id):
    try:
        directors_detail = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found'}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = DirectorSerializer(directors_detail, many=False).data
        return Response(data=data)

    elif request.method == 'DELETE':
        directors_detail.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        directors_detail.name = request.data.get('name')


@api_view(['GET', 'POST'])
def movies_list_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        data = MovieSerializer(movie).data
        return Response(data=data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title,
                                     description=description,
                                     duration=duration,
                                     director_id=director_id)


@api_view(['GET', 'PUT', 'DELETE'])
def movies_detail_view(request, id):
    try:
        movies_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'}, status=HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = MovieSerializer(movies_detail).data
        return Response(data=data)

    elif request.method == 'DELETE':
        movies_detail.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        movies_detail.title = request.data.get('title')
        movies_detail.description = request.data.get('description')
        movies_detail.duration = request.data.get('duration')
        movies_detail.director_id = request.data.get('director_id')
        return Response(status=HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def reviews_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review).data
        return Response(data=data)

    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text,
                                       movie_id=movie_id,
                                       stars=stars)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_view(request, id):
    try:
        reviews_detail = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found'}, status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewSerializer(reviews_detail).data
        return Response(data=data)

    elif request.method == 'DELETE':
        reviews_detail.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        reviews_detail.text = request.data.get('text')
        reviews_detail.movie_id = request.data.get('movie_id')
        reviews_detail.stars = request.data.get('stars')

