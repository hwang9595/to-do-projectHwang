from django.shortcuts import render
from HomeList.models import ToDoList

def incomplete_tasks(request):
   
    tasks = ToDoList.objects.filter(is_completed=False)
    return render(request, 'incomplist.html', {'tasks': tasks})