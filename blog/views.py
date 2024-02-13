"""
Views request information from the model and pass it to a template.
"""

from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.
def post_list(request):  # This view lists all the posts
    me = User.objects.get(username="aarjav")
    posts = Post.objects.filter(author=me).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": posts})
    # Essentially saying "Take the request and return the render of the template blog/post_list.html"
    # Syntax of render function: render(request, template_name, extras)
    # extras is a dictionary of variables to pass to the template


def post_detail(request, pk):  # This view displays a single post
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # commit=False means "Don't save it to the database yet"
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_edit.html", {"form": form})
