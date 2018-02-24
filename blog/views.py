from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def gedichte(request):
	gedichte = Post.objects.filter(genre="Gedichte")
	return render(request, 'blog/post_list.html', {'post': gedichte})

def kurzgeschichten(request):
	Post.objects.filter(genre="Kurzgeschichten")
	return render(request, 'blog/post_list.html', {'post': kurzgeschichten})