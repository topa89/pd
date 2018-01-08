from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from project.models import Projects
from users.forms import UserChangeForm
from users.forms import UserCreationForm
from users.models import ExtUser


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'date_of_birth',
        'email',
        'firstname',
        'is_admin',
        'lastname',
        'middlename',
    ]

    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {
            'fields': (
                'avatar',
                'date_of_birth',
                'firstname',
                'lastname',
                'middlename',
            )}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Регистрация нашей модели
admin.site.register(ExtUser, UserAdmin)
admin.site.register(Projects)
