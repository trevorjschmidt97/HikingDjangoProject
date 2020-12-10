from django.shortcuts import render
from django.http import HttpResponse
from Hikes.models import Hike
from .forms import *

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

    return render(request, 'Home/index.html')

def displayHikesPageView(request) :
    HikesList = Hike.objects.all()

    return render(request, "Hikes/displayHikes.html", {'HikesList' : HikesList})

def editHikesPageView(request) :
    HikeChoices = HikeChoiceField()
    context = {'HikeChoices' : HikeChoices}
    return render(request, "Hikes/editHike.html", context)

def storeEditHikesPageView(request) :
    if request.method=='POST':
        editHike = Hike.objects.filter(id=request.POST['Hikes']).first()

        editHike.hikerName = request.POST['hike_hiker_name']
        editHike.name = request.POST['hike_name']
        editHike.duration = request.POST['hike_duration']
        editHike.description = request.POST['hike_description']
        editHike.length = request.POST['hike_length']
        editHike.location = request.POST['hike_location']

        editHike.save()
    return render(request, 'Home/index.html')

def deleteHikeView(request) :
    if request.method=='POST':
        deleteHike = Hike.objects.filter(id=request.POST['Hikes']).first()

        deleteHike.delete()

    return render(request, 'Home/index.html')

def deleteHikePageView(request) :
    HikeChoices = HikeChoiceField()
    context = {'HikeChoices' : HikeChoices}
    return render(request, 'Hikes/deleteHike.html', context)