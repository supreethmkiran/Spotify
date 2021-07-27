from django.shortcuts import render,redirect
from .models import playlists, songs
from .forms import AddSongs,MakePlaylist,PlaylistUpdate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required
def add_song(request):     # to add songs to the database
	if request.method == 'POST':
		form = AddSongs(request.POST)
		
		if form.is_valid():         
			a= request.user
			form.instance.user= a
			form.save()
			return redirect('homepage')

	else:
		use = request.user
		form = AddSongs(instance=use)
		return render(request, 'user_details/add.html', {'form': form})

@login_required
def make_playlist(request):		#to create a new playlist for users
	if request.method == 'POST':
		form = MakePlaylist(request.POST)
		
		if form.is_valid():
			a= request.user
			form.instance.user= a
			form.save()
			return redirect('homepage')

	else:
		use = request.user
		form = MakePlaylist(instance=use)
		return render(request, 'user_details/add.html', {'form': form})

@login_required
def update_playlist(request,pk):		#to get the id of the playlist and update it accordingly
    play = playlists.objects.get(id=pk)
    form = PlaylistUpdate(instance=play)

    if request.method == 'POST':
        form = PlaylistUpdate(request.POST,instance=play)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'form':form}

    return render(request, 'user_details/add.html', context)

@login_required
def all_songs(request):					# to display all the songs on a page
    p= songs.objects.all()
    return render(request,'user_details/t.html',{'p':p})

@login_required
def update_plays(request):				# update the number of plays per song
    if request.method=="POST":
        song = request.POST["song"]
        s=songs.objects.get(song_name=song)
        s.number_of_plays +=1
        a=s.url
        s.save()
        return redirect(a)

@login_required
def my_playlists(request):			#render playlists specific to a user
    a=request.user.id
    p= playlists.objects.filter(user_id=a)
    return render(request,'user_details/playlists.html',{'p':p})

@login_required
def deletePlaylist(request,pk):			#delete a playlist
	play=playlists.objects.get(id=pk)
	play.delete()
	return redirect('/')
	
