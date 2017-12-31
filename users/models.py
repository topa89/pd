from django.db import models
from project.models import Projects

class User(models.Model):
	project = models.ForeignKey(Projects, blank=True, null = True, default=None, on_delete = models.CASCADE) 
	first_name = models.CharField(max_length = 20)
	last_name = models.CharField(max_length = 30)
	group = models.CharField(max_length = 10)
	e_mail = models.EmailField(max_length = 70, blank = True)
	password = models.CharField(max_length = 50)


	def __str__(self):
		return '{} {}'.format(self.first_name, self.last_name)
