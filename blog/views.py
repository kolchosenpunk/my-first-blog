# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'poems': Post.objects.filter(genre="Gedichte").count(), 'short_stories': Post.objects.filter(genre="Kurzgeschichten").count(), 'narratives': Post.objects.filter(genre="Erzählungen").count()})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'posts':Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date'), 'poems': Post.objects.filter(genre="Gedichte").count(), 'short_stories': Post.objects.filter(genre="Kurzgeschichten").count(), 'narratives': Post.objects.filter(genre="Erzählungen").count()})

def gedichte(request):
	gedichte = Post.objects.filter(genre="Gedichte")
	return render(request, 'blog/post_list.html', {'post': gedichte})

def kurzgeschichten(request):
	Post.objects.filter(genre="Kurzgeschichten")
	return render(request, 'blog/post_list.html', {'post': kurzgeschichten})
