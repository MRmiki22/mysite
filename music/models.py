from django.db import models

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=50)
    album_title = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    album_logo = models.CharField(max_length=1000)

class Song(models.Model):
    Album = models.ForeignKey(Album, on_delete= models.CASCADE)