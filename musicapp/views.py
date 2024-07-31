from django.shortcuts import render
from .forms import AddTrackForm
from .models import Track
def home(request, *args, **kwargs):
    tracks = Track.objects.all()
    context = {'tracks' : tracks}

    return render(request, "home.html", context)

def trackDetails(request , slug):
    my_track = Track.objects.get(slug=slug)
    context = {'track' : my_track}
    return render(request , "tracks/details.html" , context)

def addTrack(request):
    if request.method == "POST" :
        form = AddTrackForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            # render(request , "tracks/trackList.html" , {'form' : form , 'formErrors' : form.errors})
        else:
            render(request , "tracks/addTrack.html" , {'form' : form , 'formErrors' : form.errors})
    context = {'form' : AddTrackForm}
    return render(request , "tracks/addTrack.html" , context)

def deleteTrack(request , slug):
    Track.objects.get(slug=slug).delete()

def updateTrack(request , slug):
    my_track = Track.objects.filter(slug=slug).values()
    print(my_track)
    form = AddTrackForm(my_track, my_track , my_track.track_img)
    print(form)
    context = {'form' : form}
    return render(request , "tracks/addTrack.html" , context)
