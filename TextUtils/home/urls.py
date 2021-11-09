from os import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact',views.contact,name='contact'),
    path('analyze',views.analyze,name='analyze'),
]
