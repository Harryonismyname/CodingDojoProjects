from django.urls import path
from . import views

urlpatterns = [
    path('books', views.index),
    path('books/create', views.create),
    path('books/<int:id>', views.view),
    path('books/<int:id>/favorite', views.favorite),
    path('books/<int:id>/unlike', views.unlike),
    path('books/<int:id>/update', views.update),
    path('books/<int:id>/delete', views.delete)
]