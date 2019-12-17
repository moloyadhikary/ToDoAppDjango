from django import template
from app.models import ToDo


register = template.Library()


@register.simple_tag
def get_task_process(value):
    return value

