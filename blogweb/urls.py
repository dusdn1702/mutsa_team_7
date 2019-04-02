from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import blogweb.views


urlpatterns =[
    path('', blogweb.views.home, name='home'),
]