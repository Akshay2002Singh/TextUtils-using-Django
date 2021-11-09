from os import name
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('analyze',views.analyze,name='analyze'),
    path('submit_contact_form',views.submit_contact_form,name='submit_contact_form'),
]
