from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album, Song
# Create your views here.

def index(requist):
    allAlbum = Album.objects.all()
    context = {'allAlbum': allAlbum}
    return render(requist, 'music/index.html', context)

def detail(requist, album_id):
    allSong = Song.objects.filter(album = album_id)
    html = ''
    for song in allSong:
        html += '<h3>' + song.song_title+'.' + song.file_type + '</h3><br>'
    return HttpResponse(html)