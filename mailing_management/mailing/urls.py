from django.urls import path
from django.core.cache import
from django.views.decorators.cache import cache_page

from .views import MailingListView, MailingDetailView, MailingUpdateView, MailingCreateView, MailingDeleteView, \
    ClientCreateView, ClientListView, ClientUpdateView, ClientDetailView, exzample

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('detail/<int:pk>', cache_page(300)(MailingDetailView.as_view()), name='mailing_detail'),
    #path('create/', LetterCreateView.as_view(), name='letter_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', cache_page(300)(ClientListView.as_view()), name='client_list'),
    path('client_update/<int:pk>', ClientDetailView.as_view(), name='client_detail'),

    path('exzample', exzample, name='exzample')
]