from django.db import models

# Create your models here.
class Sex(models.Model):
	sex_name=models.CharField(max_length=20,default='')
