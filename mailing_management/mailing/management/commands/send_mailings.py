from datetime import datetime, date

from django.core.mail import send_mail
from django.core.management import BaseCommand

from mailing.models import Mailing
from mailing_management import settings
from mailing.models import Log


class Command(BaseCommand):
    def handle(self,  *args, **kwargs):

            mailings_obj = Mailing.objects.all()
            for mailing in mailings_obj:
                now_date = datetime.now().date()
                if mailing.date_from <= now_date <= mailing.date_to:
                    mailing.status = "start"
                    mailing.save()

                if mailing.date_to < now_date or now_date < mailing.date_from:
                    mailing.status = "end"
                    if mailing.log == None:
                        mailing.log = Log.objects.create(datetime_attempt=datetime.now(), status_attempt=True)
                    else:
                        mailing.log.datetime_attempt = datetime.now()
                        mailing.log.status_attempt = True
                    mailing.save()
            mailings = Mailing.objects.filter(status="start")
            for mailing in mailings:
                client_list = mailing.client.all()
                email_list=[client.email for client in client_list ]
                if mailing.period == "daily":
                    if datetime.now().hour == 12:
                        send_mail(
                            subject=f'{mailing.letter.title}',
                            message=f'{mailing.letter.content}',
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=email_list,
                        )
                if mailing.period == "weekly":
                    if datetime.now().day == 0:
                        send_mail(
                            subject=f'{mailing.letter.title}',
                            message=f'{mailing.letter.content}',
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=email_list,
                        )
                if mailing.period == "monthly":
                    if datetime.now().weekday() == 1:
                        send_mail(
                            subject=f'{mailing.letter.title}',
                            message=f'{mailing.letter.content}',
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=email_list,
                        )



            