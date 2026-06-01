from django.contrib import admin
from .models import ToDoList

@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')
    list_filter = ('is_completed',)
    search_fields = ('title',)