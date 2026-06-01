from django.shortcuts import render
from HomeList.models import ToDoList  # Импорт из HomeList

def incomplete_tasks(request):
    # Только НЕвыполненные задачи
    tasks = ToDoList.objects.filter(is_completed=False)
    return render(request, 'incomplist.html', {'tasks': tasks})