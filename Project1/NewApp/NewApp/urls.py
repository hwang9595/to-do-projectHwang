"""
URL configuration for NewApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HomeList import views as HomeListView
from IncompList import views as IncompListView
from CompList import views as CompListView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Списки задач
    path('', HomeListView.home_all_tasks, name='home'),
    path('complist/', CompListView.completed_tasks, name='complist'),
    path('incomplist/', IncompListView.incomplete_tasks, name='incomplist'),

    # Действия с задачами
    path('add-task/', HomeListView.add_task, name='add_task'),
    path('complete-task/<int:task_id>/', HomeListView.complete_task, name='complete_task'),
    path('delete-task/<int:task_id>/', HomeListView.delete_task, name='delete_task'),
]