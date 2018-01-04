from django.conf.urls import url

from . import views

app_name = 'project'

urlpatterns = [
    url(r'^project/$', views.index, name='index'),
    url(r'^$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutView.as_view()),
]
