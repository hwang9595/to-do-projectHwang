from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    is_completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title