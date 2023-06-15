from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requist):
    return HttpResponse("<h2> Album list </h2>")

def detail(requist):
    return HttpResponse("list of misuc")