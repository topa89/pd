from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, Template
from django.template.defaulttags import register
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .models import Projects, TodoList


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "project/login.html"
    success_url = "/"
    
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

def update_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
    user.save()

# Create your views here.
def index(request):
    context = {
        "project_info": Projects.objects.filter(id=3),
        "todo": list(TodoList.objects.filter(category=i) for i in range(len(TodoList.CATEGORY))),
        "todo2": list(TodoList.objects.filter(project=3)),

        # TODO: сделать доступ к value без создания дополнительных dict
        "category": dict(TodoList.CATEGORY[i] for i in range(len(TodoList.CATEGORY))),
        "status": dict(TodoList.STATUS[i] for i in range(len(TodoList.STATUS))),
        "importance": dict(TodoList.IMPORTANCE[i] for i in range(len(TodoList.IMPORTANCE))),
    }
    return render(request, 'project/index.html', context )

@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
