from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.http import Http404
from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ClientForm, MailingForm, LetterForm
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
    form_class = LetterForm
    success_url = reverse_lazy('mailing_create')

class LetterListView( ListView):
    model = Letter

class LetterUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model=Letter
    permission_required = 'mailing.change_letter'
    form_class = LetterForm
    success_url = reverse_lazy('mailing_list')

class LetterDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'mailing.view_letter'
    model= Letter

class LetterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Letter
    permission_required = 'mailing.delete_letter'
    success_url = reverse_lazy('mailing_list')

class ClientCreateView(LoginRequiredMixin,  CreateView): #PermissionRequiredMixin,
    model =Client
    permission_required = 'mailing.add_client'
    #fields = ['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')

class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin,UpdateView):
    model=Client
    permission_required = 'mailing.change_client'
    #fields=['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')


class ClientListView( ListView):
    model = Client

class ClientDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView):
    model=Client
    permission_required = 'mailing.view_letter'

class ClientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model=Client
    permission_required = 'mailing.delete_client'
    success_url = reverse_lazy('mailing_list')