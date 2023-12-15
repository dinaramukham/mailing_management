from django.contrib import admin

from .models import Mailing, Client, Log, Letter


# Register your models here.
@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ( 'log', 'letter', 'date_from', 'date_to', 'period', 'status',)
    search_fields = ('client', 'log', 'letter', 'date_from', 'period', 'status',)
    list_filter = ('client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message',)
    list_filter = ('name', 'email', 'message',)
    search_fields = ('name', 'email', 'message',)
@admin.register(Log)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('datetime_attempt', 'status_attempt', 'mail_response',)
    list_filter = ('datetime_attempt', 'status_attempt', 'mail_response',)
    search_fields = ('datetime_attempt', 'status_attempt', 'mail_response',)

@admin.register(Letter)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', )
    list_filter = ('title', 'content', )
    search_fields = ('title', 'content', )