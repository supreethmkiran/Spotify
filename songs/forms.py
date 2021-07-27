from django import forms
from .models import playlists,songs
from django.contrib.auth.models import User

class AddSongs(forms.ModelForm):        #a form which lets the user add a song
    class Meta:
        model = songs
        exclude = ['date_posted','number_of_plays']
        #fields = "__all__"

class MakePlaylist(forms.ModelForm):        #a form which lets the user make a playlist
    class Meta:
        model = playlists
        exclude = ['user','date_added','last_modified']
        #fields = "__all__"

class PlaylistUpdate(forms.ModelForm):          #a form which lets the user update the playlist
    class Meta:
        model = playlists
        fields = ['playlist_name', 'songs']
