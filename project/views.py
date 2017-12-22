from django.shortcuts import render

from .models import Projects, TodoList


# Create your views here.
def index(request):
    return render(request, "__base.html", {
        "project_info": Projects.objects.filter(title='Лунный ровер'),
        "todo": list(TodoList.objects.filter(category=i) for i in range(len(TodoList.CATEGORY)))
    }
                  )
