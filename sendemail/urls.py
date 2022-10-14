from django.urls import path
from .views import contactView,successView
urlpatterns=[
     path("e/",contactView,name='contactView'),
     path("s/",successView,name='success'),
   ]