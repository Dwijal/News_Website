from django.db import models

# Create your models here.
class SubCat(models.Model):

    name = models.CharField(max_length=250)
    catname = models.CharField(max_length=250)
    catid = models.IntegerField()

    def __str__(self):
        return self.name + '|' + str(self.pk)

