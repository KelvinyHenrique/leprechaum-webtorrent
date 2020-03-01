from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Torrents
from .forms import TorrentsForms

def index(request):

    username = request.POST.get('lepre_username')
    password = request.POST.get('lepre_password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home/')
    elif request.user.is_authenticated:
        return redirect('home/')
    else:
        return render(request, 'login.html')

@login_required
def home(request):
    list_ = Torrents.objects.all()
    form = TorrentsForms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'home.html', {'form': form, 'torrents': list_})

def logout_(request):
    logout(request)
    return redirect('/')
