from django.db import models

# Create your models here.
class Singers(models.Model):
	names=models.CharField(max_length=20,default='')
	ages=models.IntegerField()
	phoneNumber=models.CharField(max_length=20,default='')
	def __str__(self):
		return self.names

class Groups(models.Model):
	name=models.CharField(max_length=20,default='')
	style=models.CharField(max_length=20,default='')
	singers=models.ManyToManyField(Singers)

class Concert(models.Model):
	time=models.DateField()
	who=models.ForeignKey(Groups,on_delete=models.CASCADE)
	place=models.CharField(max_length=20,default='')