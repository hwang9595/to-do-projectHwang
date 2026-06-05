from django.shortcuts import render
from HomeList.models import ToDoList

def completed_tasks(request):
    tasks = ToDoList.objects.filter(is_completed=True)
    return render(request, 'complist.html', {'tasks': tasks})