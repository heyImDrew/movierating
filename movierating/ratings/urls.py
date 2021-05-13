from django.urls import path

from . import views

urlpatterns = [
    path('ratings', views.my_ratings, name="my_ratings"),
    path('catalog/<int:pk>/rate', views.rate, name="rate"),
]
