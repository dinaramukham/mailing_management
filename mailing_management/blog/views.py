from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, ListView, DeleteView, UpdateView

from .forms import BlogForm
from .models import Blog


# Create your views here.
class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_blog'
    model= Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog_detail')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_blog'
    model= Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog_detail')
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class BlogListView(PermissionRequiredMixin, ListView):
    model= Blog

class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'blog.view_blog'
    model= Blog
    form_class = BlogForm
    def get_object(self, queryset=None):
        self.object=super().get_object(queryset)
        self.object.count_view+=1
        self.object.save()
        return self.object
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'blog.delete_blog'
    model= Blog
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object



