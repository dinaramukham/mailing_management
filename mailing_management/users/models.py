from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    #mailing = models.ForeignKey('Mailing', on_delete=models.DO_NOTHING, blank=True,  null= True )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
