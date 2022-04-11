from unicodedata import name
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('/', views.index, name='index'),
    #music
    
    path('/<int:album_id>/', views.detail, name='detail'),
    #/music/68575/

]
