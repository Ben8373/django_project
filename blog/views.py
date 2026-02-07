from django.shortcuts import render
from django.views import generic
from .models import Post

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
    context_object_name = 'posts'

class PostDetail(generic.DetailView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "blog/post_detail.html"
    context_object_name = 'post'
