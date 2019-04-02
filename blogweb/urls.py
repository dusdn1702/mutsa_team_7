from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
import blogweb.views


urlpatterns =[
    path('', blogweb.views.home, name='home'),
    path('post/', blogweb.views.post, name='post'),
    path('post/<int:post_id>/', blogweb.views.detail, name='detail'),
    path('post/new/', blogweb.views.new, name='new'),
    path('post/create/', blogweb.views.create, name='create'),
]