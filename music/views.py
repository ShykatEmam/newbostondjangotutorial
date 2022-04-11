from  django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> THis is music app homepage</h1>")