from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField('title', max_length=50)
    summary = models.CharField('summary', max_length=50)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


    def __str__(self):
        return self.title