from django.urls import path
from . import views
from blog.models import Post
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.post_list, name='post_list'),
]