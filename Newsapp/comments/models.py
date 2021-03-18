from django.db import models

# Create your models here.
class Comments(models.Model):

    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    comments = models.TextField()
    news_id = models.IntegerField()
    date = models.CharField(max_length=250)
    time = models.CharField(max_length=250)
    status = models.IntegerField(default=0)



    def __str__(self):
        return self.comments




