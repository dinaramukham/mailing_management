from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ClientForm, MailingForm
from .models import Mailing, Letter, Client, Log
from mailing_management import settings


# Create your views here.
class MailingListView(ListView):
    model = Mailing

class MailingDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'mailing.view_mailing'
    model= Mailing

class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model=Mailing
    permission_required = 'mailing.change_mailing'
    #fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    form_class = MailingForm
    success_url = reverse_lazy('mailing_list')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
class MailingCreateView(LoginRequiredMixin, CreateView):
    model=Mailing
    form_class = MailingForm
    #fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    success_url = reverse_lazy('mailing_list')


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Mailing
    permission_required = 'mailing.delete_mailing'
    success_url = reverse_lazy('mailing_list')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
class LetterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model=Letter
    permission_required = 'mailing.add_letter'
    fields=['title','content']
    success_url = reverse_lazy('mailing_create')
class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin,CreateView):
    model =Client
    permission_required = 'mailing.add_client'
    #fields = ['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')

class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model=Client
    permission_required = 'mailing.change_letter'
    #fields=['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class ClientListView( ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model=Client
    permission_required = 'mailing.view_letter'


def exzample(request):
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
        recipient_list = mailing.client.all()
        if mailing.period == "weekly":
            if datetime.now().hour==12:
                pass
        if mailing.period=="weekly":
            if datetime.now().day==0:
                pass
        if mailing.period == "monthly":
            if datetime.now().weekday()==1:
                pass

        #send_mail(
        #    subject=f'{mailing.letter.title}',
        #    message=f'{mailing.letter.content}',
        #    from_email=settings.EMAIL_HOST_USER,
        #    recipient_list=recipient_list,
        #)

    return render(request, 'mailing/exzample.html')
