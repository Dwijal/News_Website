from django.db import models

# Create your models here.
class Manager(models.Model):

    name = models.CharField(max_length=250)
    uname = models.CharField(default="",max_length=250)
    email = models.CharField(max_length=250)
    ip = models.CharField(default="",max_length=250)
    country =models.CharField(default="",max_length=250)



    def __str__(self):
        return self.name
