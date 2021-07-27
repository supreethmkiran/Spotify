from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from songs import views as song_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('add/',song_views.add_song,name='add-songs'),
    path('update_playlist/<str:pk>/',song_views.update_playlist,name='update-playlist'),
    path('new_playlist/',song_views.make_playlist,name='new-playlist'),
    path('songs/',song_views.all_songs,name='songs'),
    path('playlists/',song_views.my_playlists,name='my-playlists'),
    path('update_plays/',song_views.update_plays,name='play_update'),
    path('delete_playlist/<str:pk>/',song_views.deletePlaylist,name='delete-playlist'),
    path('login/',auth_views.LoginView.as_view(template_name='user_details/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user_details/logout.html'), name='logout'),
]