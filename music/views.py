from cgitb import html
from  django.http import HttpResponse
from .models import Album
from django.shortcuts import render
from django.http import  Http404

def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums' : all_albums,})

def detail(request, album_id):
    try:
        album = Album.objects.get(pk = album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    
    return render(request, 'music/detail.html', {'album':album})






































def forshoppingmallsite(request):
    all_albums = Album.objects.all()
    html=''
 #1st index for music
    for album in all_albums:
        url = '/music/'+ str(album.id) +'/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'

    return HttpResponse(html)

    #return HttpResponse("<h2>Details for album_id: " + str(album_id) + "</h2>")
