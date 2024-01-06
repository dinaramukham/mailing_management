# Generated by Django 4.2.7 on 2023-12-15 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_attempt', models.DateTimeField()),
                ('status_attempt', models.BooleanField()),
                ('mail_response', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.DateField()),
                ('period', models.CharField(choices=[('daily', 'ежедневно'), ('weekly', 'раз в неделю'), ('monthly', 'раз в месяц')], default='daily', max_length=30)),
                ('status', models.CharField(choices=[('end', 'завершена'), ('create', 'создана'), ('start', 'запущена')], default='create', max_length=30)),
                ('client', models.ManyToManyField(related_name='mailing_client', to='mailing.client')),
                ('letter', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mailing.letter')),
                ('log', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mailing.log')),
            ],
        ),
    ]
