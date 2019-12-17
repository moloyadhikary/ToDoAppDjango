from django.shortcuts import render
from django.utils import timezone
from . import models
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    books = models.ToDo.objects.filter(is_completed=False).order_by('-added_date')
    stuff_for_frontend = {
        'addedTasks': books,
        'taskTypes': models.TaskType.objects.all().order_by('type_of_task')
    }
    return render(request, 'app/index.html', stuff_for_frontend)


def add_todo(request):
    text_content = request.POST["content"]
    task_type = models.TaskType.objects.get(pk= request.POST["task_type"])
    models.ToDo.objects.create(text=text_content, task_type=task_type, added_date=timezone.datetime.now())
    return HttpResponseRedirect('/')


def complete_todo(request, book_id):
    stuff_for_frontend = {
        'task': models.ToDo.objects.get(id=book_id)
    }
    return render(request, 'app/completetask.html', stuff_for_frontend)


def task_completed(request, task_id):
    task = models.ToDo.objects.get(id=task_id)
    task.is_completed = True
    task.completed_date = timezone.datetime.now()
    task.note = request.POST['complete_note']
    task.save()
    return HttpResponseRedirect('/')


def completed_tasks(request):
    stuff_for_frontend = {
        'tasks': models.ToDo.objects.filter(is_completed=True).order_by('completed_date')
    }
    return render(request, 'app/completedtasks.html', stuff_for_frontend)


def add_sub_task(request):
    task = models.ToDo.objects.get(id=request.POST['mainTaskId'])
    models.SubTask.objects.create(task_id=task, task_text=request.POST['subTaskText'], task_status='Raised')
    return HttpResponseRedirect('/')


def edit_sub_task(request, sub_task_id):
    subTask = models.SubTask.objects.get(id=sub_task_id)
    stuff_for_frontend = {
        'subTask': subTask
    }
    return render(request, 'app/edit_sub_task.html', stuff_for_frontend)


def frm_edit_sub_task(request):
    subtask = models.SubTask.objects.get(id=request.POST['id'])
    subtask.task_status = request.POST['task_status']
    subtask.task_note = request.POST['complete_note']
    subtask.task_text = request.POST['task_test']
    subtask.save()
    return HttpResponseRedirect('/')