from django.http import HttpRequest, Http404
from django.shortcuts import render

# Create your views here.
# tasks = [
#     {"id": 1, "title": "Task #1", "completed": False},
#     {"id": 2, "title": "Task #2", "completed": True},
#     {"id": 3, "title": "Task #3", "completed": False},
#     {"id": 4, "title": "Task #4", "completed": True},
#     {"id": 5, "title": "Task #5", "completed": False}
# ]

tasks = [
    {'id': 1, 'title': 'Task #1', 'description': '10 km training run', 'created': '2022-01-28 12:00',
     'updated': '2022-01-28 12:03', 'completed': False},
    {'id': 2, 'title': 'Task #2', 'description': 'English homework', 'created': '2022-01-28 12:05',
     'updated': '2022-01-28 12:07', 'completed': True},
    {'id': 3, 'title': 'Task #3', 'description': 'complete a Python homework', 'created': "2022-01-28 12:10",
     'updated': '2022-01-28 12:14', "completed": False},
    {'id': 4, 'title': 'Task #4', 'description': 'Read a book', 'created': "2022-01-28 12:15",
     'updated': '2022-01-28 12:18', 'completed': True},
    {'id': 5, 'title': 'Task #5', 'description': 'Create a new portfolio site', 'created': "2022-01-28 12:20",
     'updated': '2022-01-28 12:25', 'completed': False},
]


def task_list_view(request: HttpRequest):
    ctx = {'task_list': tasks}
    return render(request, 'task_list.html', ctx)


def task_detailed_view(request: HttpRequest, id: int):
    for task in tasks:
        if task['id'] == id:
            return render(request, 'task_detail.html', {'task': task})
    raise Http404
