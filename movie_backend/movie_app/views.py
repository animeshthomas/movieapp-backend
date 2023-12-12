from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from movie_app.serializer import MovieSerializer
from movie_app.models import Movie
from django.db.models import Q

@csrf_exempt
def viewMovies(request):
    if request.method=="POST":
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies,many=True)
        return HttpResponse(json.dumps(serializer.data))
@csrf_exempt
def addMovies(request):
    if request.method=="POST":
        data=json.loads(request.body)
        serializer=MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(json.dumps({"Status":"Success"}))
        else:
            return HttpResponse(json.dumps({"Status":"Failed"}))

@csrf_exempt
def searchMovies(request):
    if request.method == "POST":
        data = json.loads(request.body)
        received_name = data['name']
        movies = list(Movie.objects.filter(Q(name__icontains=received_name)).values())
        return HttpResponse(json.dumps(movies))
    

def deleteMovies(request):
    if request.method=="GET":
        return HttpResponse(json.dumps({"Status":"Success"}))
