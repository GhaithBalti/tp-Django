from .views import  controleform1
from .views import  controleform2
from django.urls import path

urlpatterns=[
     path("p",controleform1,name='controleform1'),
   ]
urlpatterns=[
     path("p2",controleform2,name='controleform2'),
   ]
urlpatterns=[
     path("p3",controleform2,name='controleform3'),
   ]