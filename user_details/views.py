from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect

from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm 
from django.contrib import messages

# Create your views here.

def homepage(request):                  #render site landing page
	return render(request,'user_details/homepage.html')

# def homepage1(request):
# 	return render(request,'user_details/homepage.html')

def register(request):                      #to save data when a new user registers 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('homepage')
    else:
        form = UserRegisterForm()
    return render(request, 'user_details/register.html', {'form': form})

