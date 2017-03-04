from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Contact(models.Model):
	name=models.CharField(max_length=100)
	contact_number=models.CharField(max_length=10)
	address=models.TextField()
	issue_date=models.DateTimeField('date request sent')
	def _str_(self):
		return self.name



class Portfolio(models.Model):	
	name_of_user=models.CharField(max_length=100)
	work_ex=models.IntegerField()	
	content=model.TextField()
	area_of_spl=model.CharField(max_length=250)
	def _str_(self):
		return self.name_of_user



# Create your models here.
