from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoList

def home_all_tasks(request):
    # Отдаем вообще все задачи на главную
    tasks = ToDoList.objects.all()
    return render(request, 'home.html', {'tasks': tasks})

def add_task(request):
    if request.method == "POST":
        task_title = request.POST.get("title", "").strip()
        if task_title:
            ToDoList.objects.create(title=task_title)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def complete_task(request, task_id):
    task = get_object_or_404(ToDoList, id=task_id)
    task.is_completed = not task.is_completed  # Переключает туда и обратно
    task.save()
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def delete_task(request, task_id):
    task = get_object_or_404(ToDoList, id=task_id)
    task.delete()
    return redirect(request.META.get('HTTP_REFERER', 'home'))