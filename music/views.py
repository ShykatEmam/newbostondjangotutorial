from  django.http import HttpResponse
from .models import Album

def index(request):
    return HttpResponse("<h1> THis is music app homepage</h1>")

def detail(request, album_id):
    return HttpResponse("<h2>Details for album_id: " + str(album_id) + "</h2>")

