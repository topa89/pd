from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

app_name = 'project'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^info/$', views.todo_info, {'list_id':'pk'}),
    	]