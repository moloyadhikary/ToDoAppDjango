from django.db import models


class TaskType(models.Model):
    type_of_task = models.CharField(max_length=200)


class ToDo(models.Model):
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE, default=1)
    added_date = models.DateTimeField(null=False)
    text = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(null=True)
    note = models.CharField(max_length=500, blank=True)


class SubTask(models.Model):
    task_id = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    task_text = models.CharField(max_length=200)
    task_note = models.CharField(max_length=200, blank=True)
    task_status = models.CharField(max_length=20)
