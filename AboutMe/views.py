from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Welcome to AboutMe Universe!')

def searchPageView(request):
    return HttpResponse('This is the search page')