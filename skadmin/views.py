from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView


def home(request):
    return render(request, 'test.html')