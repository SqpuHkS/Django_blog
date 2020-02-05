from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.views.generic import View
from .models import *
from .utils import *
from .forms import TagForm, PostForm


def main_page(request):
    data = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': data})

def tags_list(request):
    data = Tag.objects.all()
    return render(request, 'blog/tags.html', context={'tags':data})



class TagUpdate(ObjectUpdateMixin, View):
    model_form = TagForm
    model = Tag
    template = 'blog/tag_update.html'

class PostUpdate(ObjectUpdateMixin, View):
    model_form = PostForm
    model = Post
    template = 'blog/post_update.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'blog/tag_create.html'

class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'blog/post_create_form.html'

class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'blog/post_delete.html'
    redirect_url = 'posts_list_url'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'blog/tag_delete.html'
    redirect_url = 'tags_list_url'