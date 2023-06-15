from django.shortcuts import render
from django.http import HttpResponse
from .models import Album, Song
# Create your views here.

def index(requist):
    allAlbum = Album.objects.all()
    html = ''
    for album in allAlbum:
        url = '/music/' + str(album.id) + '/'
        html += ' <a href = "'+url+'">'+ album.album_title +' </a><br>'
    return HttpResponse(html)

def detail(requist, album_id):
    return HttpResponse("<h2> Music list for album id: "+ str(album_id) + " </h2>")