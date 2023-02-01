"""
Task application URL Configuration
"""

from django.urls import path
from task.views import task_list_view, task_detailed_view

urlpatterns = [
    path('', task_list_view, name='task-list'),
    path('<int:id>/', task_detailed_view, name='task-detail')
]
