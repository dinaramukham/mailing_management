from django.shortcuts import render
from django.urls import  reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Mailing, Letter


# Create your views here.
class MailingListView(ListView):
    model = Mailing

class MailingDetailView(DetailView):
    model= Mailing
class LetterCreateView(CreateView):
    model=Letter
    fields=['title','content']
    success_url = reverse_lazy('mailing_create')
class MailingUpdateView(UpdateView):
    model=Mailing
    fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    success_url = reverse_lazy('mailing_list')
class MailingCreateView(CreateView):
    model=Mailing
    fields=['client', 'log', 'letter', 'date_from', 'date_to', 'period', 'status']
    success_url = reverse_lazy('mailing_list')

class MailingDeleteView(DeleteView):
    model=Mailing
    success_url = reverse_lazy('mailing_list')