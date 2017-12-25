from django.shortcuts import render
from django.template.defaulttags import register
from django.template import Template, Context
from .models import Projects, TodoList
from django.http import HttpResponse



# Create your views here.
def index(request):
    return render(request, "__base.html", {
        "project_info": Projects.objects.filter(title='Лунный ровер'),
        "todo": list(TodoList.objects.filter(category=i) for i in range(len(TodoList.CATEGORY))),

        # TODO: сделать доступ к value без создания дополнительных dict
        "category": dict(TodoList.CATEGORY[i] for i in range(len(TodoList.CATEGORY))),
        "status": dict(TodoList.STATUS[i] for i in range(len(TodoList.STATUS))),
        "importance": dict(TodoList.IMPORTANCE[i] for i in range(len(TodoList.IMPORTANCE))),
    },
                  )

def list_info(request):
    t = Template("<html><body>It is now {{ todo_list }}</body></html>")
    html = t.render(Context({'todo_list': 12}))
    return HttpResponse(html)


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)

