from django.shortcuts import render
from HomeList.models import ToDoList  # Импорт из HomeList

def completed_tasks(request):
    # Только ВЫполненные задачи
    tasks = ToDoList.objects.filter(is_completed=True)
    return render(request, 'complist.html', {'tasks': tasks})