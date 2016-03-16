from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import SongForm
from models import Song


# Create your views here.

def songs(request):
    if request.method == 'POST':
        song_form = SongForm(request.POST, prefix='song')
        if song_form.is_valid():
            song_form.save()
    else:
        song_form = SongForm()
    return render(request, 'songs.html', {'song_form': song_form,
                                          'songs': Song.objects.all()})