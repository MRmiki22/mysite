from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# Create your views here.

def index(requist):
    allAlbum = Album.objects.all()
    return render(requist, 'music/index.html', {'allAlbum': allAlbum})

def detail(requist, album_id):
    album = get_object_or_404(Album, pk=album_id)
    allsong = album.song_set.all()
    return render(requist, 'music/detail.html', {'allsong': allsong, 'album': album})