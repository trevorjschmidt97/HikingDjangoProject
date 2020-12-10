from django.urls import path
from .views import indexPageView
from .views import createPageView
from .views import storeHikePageView
from .views import displayHikesPageView

urlpatterns = [
    path("", indexPageView, name="index"),   
    path("create", createPageView, name='createHike'), 
    path('store', storeHikePageView, name='storeHike'),
    path('display', displayHikesPageView, name='displayHikes')
]                  
