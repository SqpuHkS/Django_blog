from django.shortcuts import render
from .models import *

def main_page(request):
    data = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': data})

def post_detail(request, slug):
    data = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post': data})

def tags_list(request):
    data = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags':data})

def tag_detail(request, slug):
    data = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag':data})