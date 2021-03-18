from django.db import models

# Create your models here.
class Contactform(models.Model):
    
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    body = models.TextField()
    date = models.CharField(max_length=250, default='-')
    time = models.CharField(max_length=250, default='-')





    def __str__(self):
        return self.name




