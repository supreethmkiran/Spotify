from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class songs(models.Model):                  #to save the details of a song
    song_name = models.CharField(max_length=200)
    artists = models.CharField(max_length=500)
    duration = models.DecimalField(max_digits=20,decimal_places=2)
    number_of_plays = models.IntegerField(default=0)
    url = models.URLField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.song_name

class playlists(models.Model):              #to save the details of a playlist
    playlist_name = models.CharField("Playlist Name",max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date_added = models.DateTimeField(default=timezone.now)
    last_modified = models.DateField(auto_now=True,blank=True)
    songs = models.ManyToManyField(songs)

    def __str__(self):
        return self.playlist_name

