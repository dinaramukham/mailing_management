from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        user= User.objects.create(
            first_name='admin', email='admin@mail.ru',
            is_staff=True, is_superuser=True,
        )
        user.set_password('some_password')
        user.save()