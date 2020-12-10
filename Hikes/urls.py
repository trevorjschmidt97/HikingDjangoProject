from django.urls import path
from .views import *

urlpatterns = [
    path("", indexPageView, name="index"),   
    path("create", createPageView, name='createHike'), 
    path('store', storeHikePageView, name='storeHike'),
    path('display', displayHikesPageView, name='displayHikes'),
    path('edit', editHikesPageView, name='editHike'),
    path('storeEdit', storeEditHikesPageView, name='storeEditHike'),
    path('delete', deleteHikePageView, name='deleteHike'),
    path('deleteFinal', deleteHikeView, name='deleteFinal')
]                  
