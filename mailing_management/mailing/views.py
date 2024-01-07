from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ClientForm, MailingForm
from .models import Mailing, Letter, Client


# Create your views here.
class MailingListView(ListView):
    model = Mailing

class MailingDetailView(DetailView):
    model= Mailing
class MailingUpdateView(UpdateView):
    model=Mailing
    #fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    form_class = MailingForm
    success_url = reverse_lazy('mailing_list')
class MailingCreateView(CreateView):
    model=Mailing
    form_class = MailingForm
    #fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    success_url = reverse_lazy('mailing_list')


class MailingDeleteView(DeleteView):
    model=Mailing
    success_url = reverse_lazy('mailing_list')

class LetterCreateView(CreateView):
    model=Letter
    fields=['title','content']
    success_url = reverse_lazy('mailing_create')
class ClientCreateView(CreateView):
    model =Client
    #fields = ['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')

class ClientUpdateView(UpdateView):
    model=Client
    #fields=['name', 'email', 'message']
    form_class = ClientForm
    success_url = reverse_lazy('mailing_list')

class ClientListView(ListView):
    model = Client
class ClientDetailView(DetailView):
    model=Client
