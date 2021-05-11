import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from enums.errors import ErrorsEnum
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import requests

from users.models import UserProfile


def login(request):
    if request.method == "POST":
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('catalog')
        return render(request, 'auth/login.html', {"error": ErrorsEnum.USER_NOT_FOUND.value})
    return render(request, 'auth/login.html', {"error": False})


def registration(request):
    if request.method == "POST":
        username = request.POST.get('login')
        password = request.POST.get('password')
        if not User.objects.filter(username=username):
            user = User.objects.create_user(username, '', password)
            user.save()
            return render(request, 'auth/login.html', {"error": False, "message": True})
        return render(request, 'auth/registration.html', {"error": ErrorsEnum.USER_ALREADY_EXISTS.value})
    if request.method == "GET":
        return render(request, 'auth/registration.html', {"error": False})


def logout(request):
    auth_logout(request)
    return redirect('login')

def my_account(request):
    if request.method == "GET":
        data = requests.get("http://worldtimeapi.org/api/timezone/Europe/Minsk.json").json()
        return render(request, 'catalog/account.html', {
            'client_ip': data.get('client_ip'),
            'location': data.get('timezone'),
            'local_time': datetime.datetime.now(),
            'is_admin': request.user.is_staff,
            'account': request.user,
            'profile': UserProfile.objects.get(user=request.user)
        })

def edit(request):
    if request.method == "GET":
        return render(request, 'auth/edit.html', {
            'account': request.user,
            'profile': UserProfile.objects.get(user=request.user)
        })
    if request.method == "POST":
        return render(request, 'auth/edit.html', {
            'account': request.user,
            'profile': UserProfile.objects.get(user=request.user)
        })