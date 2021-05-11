from django.urls import path
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='catalog'), name='index'),
    path('catalog', views.catalog, name="catalog"),
    path('catalog/<int:pk>', views.film, name="film"),
]
