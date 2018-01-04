from django.contrib.auth.models import User
from django.db import models

from project.models import Projects, Group


class Users(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null = True, default = None,)
	project = models.ForeignKey(Projects, blank=True, null = True, default = None, on_delete = models.CASCADE) 
	group = models.ForeignKey(Group, blank = True, null = True, default = None, on_delete = models.CASCADE )





