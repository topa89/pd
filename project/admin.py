from django.contrib import admin
from .models import Projects, TodoList, Group
from users.models import User

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']
	

class UserAdmin(admin.ModelAdmin):
	list_display =('__str__', 'group', 'e_mail')
	list_filter = ['project']



admin.site.register(Projects, TodoAdmin)
admin.site.register(TodoList)
admin.site.register(Group)
admin.site.register(User, UserAdmin)