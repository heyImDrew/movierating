from django.urls import path

from . import views

urlpatterns = [

    path('auth/login', views.login, name="login"),
    path('auth/registration', views.registration, name="registration"),
    path('auth/logout', views.logout, name="logout"),

    path('account', views.my_account, name="my_account"),
    path('account/edit', views.edit, name="edit"),
    path('account/edit/password', views.change_password, name="change_password"),

]
