from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.context_processors import csrf
from django.template.defaulttags import register
from django.views.generic.base import View
from django.views.generic.edit import FormView

from .models import Projects, TodoList


# noinspection PyAttributeOutsideInit
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "project/login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        super(LoginFormView, self).form_valid(form)
        context = {
            "project_info": Projects.objects.filter(title=self.user.users.project),
            "todo": list(TodoList.objects.filter(category=i, project=self.user.users.project) for i in
                         range(len(TodoList.CATEGORY))),

            # TODO: сделать доступ к value без создания дополнительных dict
            "category": dict(TodoList.CATEGORY[i] for i in range(len(TodoList.CATEGORY))),
            "status": dict(TodoList.STATUS[i] for i in range(len(TodoList.STATUS))),
            "importance": dict(TodoList.IMPORTANCE[i] for i in range(len(TodoList.IMPORTANCE))),
        }
        context.update(csrf(self.request))
        return render(self.request, 'project/index.html', context)


class LogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect("/")


# Create your views here.
def index(request):
    return render(request, 'project/index.html')


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
