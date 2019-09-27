from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('wof.html/',views.wof,name='wof')
]

