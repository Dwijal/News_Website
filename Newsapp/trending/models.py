from django.db import models

# Create your models here.
class Trending(models.Model):

    headline = models.CharField(max_length=250)


    def __str__(self):
        return self.headline
