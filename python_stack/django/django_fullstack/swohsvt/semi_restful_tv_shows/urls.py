from django.urls import path
from . import views
urlpatterns =[
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.new),
    path('shows/<int:id>', views.about),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:id>/destroy', views.destroy),
    path('shows/<int:id>/update', views.update),
    path('shows/new/create', views.create)
]