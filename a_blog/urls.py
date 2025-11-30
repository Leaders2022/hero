from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.blog,name='blog'),
    path('post',views.post,name='post'),
]