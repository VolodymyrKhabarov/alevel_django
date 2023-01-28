from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def register_view(request: HttpRequest):
    return render(request, 'register.html')


def login_view(request: HttpRequest):
    return render(request, 'login.html')
