"""
User application URL Configuration
"""

from django.urls import path
from user.views import login_view, register_view

urlpatterns = [
    path('register/', register_view, name='registration'),
    path('login/', login_view, name='login')
]
