from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name = 'index'),
    path('home/',views.home, name = 'home'),
    path('form/',views.regis_form, name = 'form'),
    path('merit/',views.merit,name = 'merit'),
    path('courses/',views.courses,name = 'courses'),
    path('about/',views.about,name = 'about'),
    
]