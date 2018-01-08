from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users.models import Users
from .models import Projects, TodoList, Group, ProjectCategories


# Register your models here.
class ProjectUsers(admin.TabularInline):
    model = Users
    fk_name = "project"
    fields = ['group', 'user']
    can_delete = False
    verbose_name_plural = 'Студенты'


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectUsers
    ]


class DopUserInfo(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = 'Дополнительно'


class UsersAdmin(BaseUserAdmin):
    inlines = [DopUserInfo]


class TodoListAdmin(admin.ModelAdmin):
    list_filter = ['project', 'category']
    list_display = ['project', 'category', 'title']


admin.site.unregister(User)
admin.site.register(User, UsersAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(TodoList, TodoListAdmin)
admin.site.register(Group)
admin.site.register(ProjectCategories)
