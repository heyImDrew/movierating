from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name="login"),
    path('registration', views.registration, name="registration"),
    path('logout', views.logout, name="logout"),
    path('my_account', views.my_account, name="my_account"),
    path('edit', views.edit, name="edit"),
]
