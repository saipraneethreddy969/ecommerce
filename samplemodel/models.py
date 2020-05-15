from django.db import models
from datetime import date
# Create your models here.
class name(models.Model):
    surname=models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    option=models.BooleanField(default=False)
    date=models.DateField(auto_now=False,blank=True)
    def __str__(self):
        return self.firstname


class Farmer(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
     
    def __str__(self):
        return self.name

class crops(models.Model):
    farmer=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    essentialcrop=models.CharField(max_length=50,default=None)
    crops=models.TextField()
    
    def __str__(self):
        return self.essentialcrop

class movies(models.Model):
    moviename=models.CharField(max_length=100)
    def __str__(self):
        return self.moviename
class actors(models.Model):
    actorname=models.CharField(max_length=100)
    movies=models.ManyToManyField(movies)
    def __str__(self):
        return self.actorname
