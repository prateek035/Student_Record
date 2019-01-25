from django.db import models

# Create your models here.


class School(models.Model):
	sname       = models.CharField(max_length = 100)
	affiliation = models.CharField(max_length = 10, default = "CBSE") 

	def __str__(self):
		return self.sname




class Book(models.Model):
	title     =  models.CharField(max_length = 100)
	publisher =  models.CharField(max_length = 50,default = "GOD")

	def __str__(self):
		return self.title



class Student(models.Model):
	sid        = models.IntegerField(default = 0)
	fname      = models.CharField(max_length = 35)
	lname      = models.CharField(max_length = 35)
	email      = models.EmailField(max_length = 254)
	gender     = models.CharField(max_length = 10)
	school     = models.ForeignKey(School ,on_delete = models.CASCADE)
	book       = models.ManyToManyField(Book)

	def __str__(self):
		return self.fname + " " + self.lname






