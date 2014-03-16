from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Movie

def home_page(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        movie_name = request.POST.get('movie_name', "")
        Movie.objects.create(name = movie_name)
    else:
        return HttpResponse("NOT SUPPORTED")
    movies = Movie.objects.all()
    return render(request, "home.html", {'movies': movies})