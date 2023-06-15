from django.db import models

# Create your models here.
class Album(models.Model):
    genre = models.CharField(max_length=50)
    album_title = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.album_title + ' by ' + self.artist_name

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete= models.CASCADE)
    song_title = models.CharField(max_length=50, default= 0)
    file_type = models.CharField(max_length=10, default= 0)
    is_fav = models.BooleanField(default = False)
    def __str__(self):
        return self.song_title + '.' + self.file_type;