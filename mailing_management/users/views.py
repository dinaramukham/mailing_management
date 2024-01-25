from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import UserRegisterForm, UserForm
from .models import User
from mailing_management import settings


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailing_list')
    
    def form_valid(self, form):
        new_user=form.save()
        send_mail(
            subject= 'Поздравляем, вы зарегестрированы',
            message= 'Вы зарегистрированы',
            from_email = settings.EMAIL_HOST_USER,
            recipient_list = [new_user.email ]

        )
        return super().form_valid(form)

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class=UserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailing_list')
class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('mailing_list')