from django.db import models

class Product(models.Model):
	serial = models.IntegerField()
	id = models.CharField(max_length = 200, primary_key = True)
	engName = models.CharField(max_length = 200, default = 'N/A')
	vieName = models.CharField(max_length = 200, default = 'N/A')
	bard = models.CharField(max_length = 50,default = 'N/A')
	size = models.CharField(max_length = 50,default = 'N/A')
	price = models.IntegerField()
	exp = models.CharField(max_length = 20)
	uses = models.CharField(max_length = 1000)
	manuals = models.CharField(max_length = 1000)
	origin = models.CharField(max_length = 50)
	urlInfo = models.CharField(max_length = 50)
	publish = models.CharField(max_length = 50)
	
	def __str__(self):
		return vieName + '|' + engName
