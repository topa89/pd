from django.conf.urls import  url, include
from django.views.generic import ListView, DetailView
from project.models import Projects

urlpatterns = [
	url(r'^$', ListView.as_view(queryset=Projects.objects.all(), 
		template_name="user.html")),
]