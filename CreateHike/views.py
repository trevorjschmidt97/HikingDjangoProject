from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Welcome to CreateHike Universe!')