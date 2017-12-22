from django.contrib import admin

from .models import Projects, TodoList

# Register your models here.

admin.site.register(Projects)
admin.site.register(TodoList)