from django.db import models

# Create your models here.


class Services(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.name


class Customers(models.Model):
    firstname = models.CharField(max_length=30, blank=False, default='')
    lastname = models.CharField(max_length=30, blank=False, default='')
    phone =  models.CharField(max_length=11, blank=False, default='')
    services = models.ManyToManyField(Services, blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname
