from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Projects, TodoList, Group
from users.models import Users

# Register your models here.
class ProjectUsers(admin.TabularInline):
	model = Users
	fk_name = "project"
	fields = ['first_name', 'last_name', 'group',]


class ProjectAdmin(admin.ModelAdmin):
	inlines=[
		ProjectUsers
	]

class DopUserInfo(admin.StackedInline):
	model = Users
	can_delete = False
	verbose_name_plural = 'Дополнительно'

class UsersAdmin(BaseUserAdmin):
	inlines = [DopUserInfo]


admin.site.unregister(User)
admin.site.register(User, UsersAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(TodoList)
admin.site.register(Group)