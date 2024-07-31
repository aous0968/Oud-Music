from django.shortcuts import render
from musicapp.models import Track
def index(request):
    
    context = {}

    return render(request, "controlPanleBase.html", context)

def TracksControlPanle(request):
    tracks = Track.objects.all()
    context = {'tracks' : tracks}

    return render(request, "tracksControlPanle.html", context)