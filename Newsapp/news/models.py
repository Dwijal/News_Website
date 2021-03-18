from django.db import models

# Create your models here.
class News(models.Model):

    name = models.CharField(max_length=250)
    summary = models.TextField()
    body = models.TextField()
    date = models.DateField()
    picname = models.FileField()
    picurl = models.FileField()
    author = models.CharField(max_length=250)
    catname = models.CharField(max_length=250, default='-')
    catid = models.IntegerField(default=0)
    ocatid = models.IntegerField(default=0)
    show = models.IntegerField(default=0)
    tags = models.TextField(default="")
    act = models.IntegerField(default=0)
    rand = models.IntegerField(default=0)


    def __str__(self):
        return self.name + '|' + str(self.pk)

