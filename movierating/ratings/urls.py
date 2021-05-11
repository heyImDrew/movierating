from django.urls import path

from . import views

urlpatterns = [
    path('my', views.my_ratings, name="my_ratings"),
    path('<int:pk>', views.rate, name="rate"),
]
