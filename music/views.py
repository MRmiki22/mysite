from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requist):
    return HttpResponse("<h2> Album list </h2>")

def detail(requist, album_id):
    return HttpResponse("<h2> Music list </h2>")