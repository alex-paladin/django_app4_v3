from django.shortcuts import render, get_object_or_404

# Create your views here.

from apps.posts.models import Post


def post_list(request):
    posts = Post.objects.filter(status='p').order_by('created_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status='p')
    return render(request, 'posts/post_detail.html', {'post': post})