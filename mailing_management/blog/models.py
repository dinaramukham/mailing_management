from datetime import datetime

from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150)
    message = models.TextField()
    photo = models.ImageField(upload_to='media/')
    count_view = models.IntegerField(default=0 )
    date_publication = models.DateField(default=datetime.now().date())
