from django.db import models

class Task(models.Model):
    title = models.CharField('title', max_length=50)
    summary = models.CharField('summary', max_length=50)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


    def __str__(self):
        return self.title