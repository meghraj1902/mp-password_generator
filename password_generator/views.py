from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'password_generator/home.html')

def about(request):
    return render(request, 'password_generator/about.html')

def password(request):

    thepassword = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'), 12)

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*?"_-"'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'password_generator/password.html', {'password':thepassword})
