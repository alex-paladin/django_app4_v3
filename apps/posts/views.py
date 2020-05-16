from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DeleteView, DetailView, UpdateView
from django.urls.base import reverse_lazy
from apps.posts.models import Post

# Create your views here.

class PostListView(ListView):
    paginate_by = 3
    queryset = Post.objects.filter(status='p').order_by('-created_at')

class PostDetailView(DetailView):
    queryset = Post.objects.filter(status='p').order_by('-created_at')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'posts/post_delete.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','text']
    success_url = reverse_lazy('post_list')
    template_name_suffix = '_update_form'
