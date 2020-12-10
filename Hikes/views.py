from django.shortcuts import render
from django.http import HttpResponse
from Hikes.models import Hike

def indexPageView(request) :
    return render(request, 'Hikes/index.html') 

def createPageView(request) :
    return render(request, 'Hikes/createHike.html')

def storeHikePageView(request) :
    if request.method == 'POST' :
        newHike = Hike()

        newHike.hikerName = request.POST['hike_hiker_name']
        newHike.name = request.POST['hike_name']
        newHike.duration = request.POST['hike_duration']
        newHike.description = request.POST['hike_description']
        newHike.length = request.POST['hike_length']
        newHike.location = request.POST['hike_location']

        newHike.save()

    return render(request, "Home/index.html")

def displayHikesPageView(request) :
    return render(request, "Hikes/displayHikes.html")
