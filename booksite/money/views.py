from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def index(request):
    data = {
        'title': 'Головна сторінка',
    }
    return render(request, 'money/index.html', data)

def about(request):
    return render(request, 'money/about.html')