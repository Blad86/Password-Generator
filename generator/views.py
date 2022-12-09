from django.shortcuts import render
from django.http import HttpResponse
import random
import requests


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    characters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('uppercace'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    lendth = int(request.GET.get('lendth', 12))
    thepassword=''
    for i in range(lendth):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})


def More(request):
    return render(request, 'generator/More.html')
