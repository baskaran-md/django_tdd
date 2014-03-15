from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home_page(request):
    if request.method == 'POST':
        movie_name = request.POST['movie_name']
        return render(request, "home.html", { 'movie_name':movie_name })
    return render(request, "home.html")
    #return HttpResponse("<html><title>Movie List</title><h1>My Movie List</h1></html>")
