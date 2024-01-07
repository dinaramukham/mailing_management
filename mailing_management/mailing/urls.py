from django.urls import path

from .views import MailingListView, MailingDetailView, MailingUpdateView, MailingCreateView, MailingDeleteView, \
    ClientCreateView, ClientListView, ClientUpdateView, ClientDetailView

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    #path('create/', LetterCreateView.as_view(), name='letter_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_update/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
]