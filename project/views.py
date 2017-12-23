from django.shortcuts import render
from django.template.defaulttags import register

from .models import Projects, TodoList


# Create your views here.
def index(request):
    return render(request, "__base.html", {
        "project_info": Projects.objects.filter(title='Лунный ровер'),
        "todo": list(TodoList.objects.filter(category=i) for i in range(len(TodoList.CATEGORY))),
        "category": dict(TodoList.CATEGORY[i] for i in range(len(TodoList.CATEGORY))),
        "status": dict(TodoList.STATUS[i] for i in range(len(TodoList.STATUS))),
        "importance": dict(TodoList.IMPORTANCE[i] for i in range(len(TodoList.IMPORTANCE))),

    },
                  )


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
