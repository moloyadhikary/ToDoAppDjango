from django.conf.urls import url
from django.urls import path
from app import views

urlpatterns = [
  path('', views.home, name='home'),
  path('add_todo', views.add_todo, name='add_todo'),
  path('complete_todo/<int:book_id>', views.complete_todo),
  path('<int:task_id>/task_completed', views.task_completed, name='task_completed'),
  path('completed_tasks', views.completed_tasks),
  path('add_sub_task', views.add_sub_task),
  path('edit_sub_task/<int:sub_task_id>', views.edit_sub_task),
  path('frm_edit_sub_task', views.frm_edit_sub_task)
]
