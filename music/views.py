from django.shortcuts import render
from django.http import Http404
from .models import Album, Song
# Create your views here.

def index(requist):
    allAlbum = Album.objects.all()
    return render(requist, 'music/index.html', {'allAlbum': allAlbum})

def detail(requist, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album not found")
    allsong = album.song_set.all()
    return render(requist, 'music/detail.html', {'allsong': allsong, 'album': album})