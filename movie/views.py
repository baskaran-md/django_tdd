from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home_page(request):
    return render(request, "home.html")
    #return HttpResponse("<html><title>Movie List</title><h1>My Movie List</h1></html>")
