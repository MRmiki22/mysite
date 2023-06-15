from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# Create your views here.

def index(requist):
    allAlbum = Album.objects.all()
    return render(requist, 'music/index.html', {'allAlbum': allAlbum})

def detail(requist, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(requist, 'music/detail.html', {'album': album})

def fav(requist, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk = requist.POST['song'])
    except(keyError, Song.DoesNotExit):
        return render(requist, 'music/detail.html', {'album': album, 'error_message': "No valid selection"})
    else:
        if selected_song.is_fav:
            selected_song.is_fav = False
        else:
            selected_song.is_fav = True
        selected_song.save()
        return render(requist, 'music/detail.html', {'album': album})
