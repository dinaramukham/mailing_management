
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import BlogDetailView, BlogCreateView, BlogDeleteView, BlogUpdateView, BlogListView

urlpatterns = [
    path('blog_detail/<int:pk>', cache_page(300)(BlogDetailView.as_view()), name='blog_detail'),
    path('blog_create/<int:pk>', BlogCreateView.as_view(), name='blog_create'),
    path('blog_delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_list/<int:pk>', BlogListView.as_view(), name='blog_list'),
]