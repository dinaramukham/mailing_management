from django.db import models


# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(null=True, blank=True)


class Mailing(models.Model):
    client = models.ManyToManyField('Client', related_name='mailing_client')
    log = models.OneToOneField("Log", on_delete=models.CASCADE, null=True, blank=True)
    letter = models.OneToOneField('Letter', on_delete=models.CASCADE)
    date_from = models.DateField()
    date_to = models.DateField()
    period = models.CharField(max_length=30, default="daily", choices=(
        ("daily", "ежедневно",), ("weekly", "раз в неделю",), ("monthly", "раз в месяц",),
    ), )
    status = models.CharField(max_length=30, default="create", choices=(
        ("end", "завершена",), ("create", "создана",), ("start", "запущена",),
    ), )


class Letter(models.Model):

    title = models.CharField(max_length=50, )
    content = models.TextField()


class Log(models.Model):
    datetime_attempt = models.DateTimeField()
    status_attempt = models.BooleanField()
    mail_response = models.TextField(blank=True) # ?!
