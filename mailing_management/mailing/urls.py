from django.urls import path

from django.views.decorators.cache import cache_page

from .views import MailingListView, MailingDetailView, MailingUpdateView, MailingCreateView, MailingDeleteView, \
    ClientCreateView, ClientListView, ClientUpdateView, ClientDetailView, LetterCreateView, LetterListView, \
    LetterDetailView, LetterUpdateView

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('detail/<int:pk>', cache_page(300)(MailingDetailView.as_view()), name='mailing_detail'),
    #path('create/', LetterCreateView.as_view(), name='letter_create'),
    path('update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing_create/', MailingCreateView.as_view(), name='mailing_create'),
    path('delete/<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),

    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_list/', cache_page(300)(ClientListView.as_view()), name='client_list'),
    path('client_detail/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client_update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),

    path('letter_create/', LetterCreateView.as_view(), name='letter_create'),
    path('letter_list/', cache_page(300)(LetterListView.as_view()), name='letter_list'),
    path('letter_detail/<int:pk>', LetterDetailView.as_view(), name='letter_detail'),
    path('letter_update/<int:pk>', LetterUpdateView.as_view(), name='letter_update'),

]