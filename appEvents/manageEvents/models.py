from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Events(models.Model):
    event_name = models.CharField(max_length=100)
    event_date = models.DateField()
    event_description = models.TextField()
    subscribe = models.ManyToManyField(User, related_name='subscribe', blank=True)
    def __str__ (self):
        return self.event_name
    def total_subs (self):
        return self.subscribe.count()


#options to contact form
bussines_options = [
    [0, "Consult"],
    [1, "Sugest"],
    [2, "Others"] 
]
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    bussines_type = models.IntegerField(choices=bussines_options)
    comments =  models.TextField()
    #notify = models.BooleanField()
    def __str__(self):
        return self.name
        