import datetime

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from enums.errors import ErrorsEnum
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import requests

from ratings.models import Review
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
        data = {
            'films_rated': len(Review.objects.filter(user=request.user)),
            'average_rating': round(sum([review.rating for review in Review.objects.filter(user=request.user)]) /
                len(Review.objects.filter(user=request.user)), 2),
            'is_admin': request.user.is_staff,
            'account': request.user,
            'profile': UserProfile.objects.get(user=request.user)
        }
        data.update(api_response("Minsk"))
        return render(request, 'catalog/account.html', data)


def api_response(city):
    data = requests.get(f"https://worldtimeapi.org/api/timezone/Europe/{city}.json").json()
    return {
        'client_ip': data.get('client_ip'),
        'location': data.get('timezone'),
        'local_time': datetime.datetime.now(),
    }


def edit(request):
    if request.method == "GET":
        return render(request, 'auth/edit.html', {
            'account': request.user,
            'profile': UserProfile.objects.get(user=request.user)
        })
    if request.method == "POST":
        usr = UserProfile.objects.get(user=request.user)
        email = request.POST.get('email')
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        if email:
            usr.email = email
        if name:
            request.user.first_name = name
        if surname:
            request.user.last_name = surname
        usr.save()
        request.user.save()
        return redirect('my_account')


def change_password(request):
    if request.method == "GET":
        return render(request, 'auth/changepass.html')
    if request.method == "POST":
        password = request.POST.get('password')
        retype_password = request.POST.get('retype-password')
        if password == retype_password:
            request.user.set_password(password)
            request.user.save()
            return redirect('logout')
        return render(request, 'auth/changepass.html', {
            "message": False,
            "error": ErrorsEnum.PASSWORDS_NOT_MATCH.value
        })
