from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('home/message', views.make_post),
    path('home/comment', views.make_comment)

]