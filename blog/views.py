from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request): ## request parameter is required by all views.
    posts = Post.published.all()

    return render(request, 'blog/post/list.html', {'posts':posts})
    ##Using the redner() shortcut provided by Django to render the list of posts  with the given template.
    ##It returns an HttpResponse object with the rendered text (normally, HTML code).
# Create your views here.

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})