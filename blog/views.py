"""
Views request information from the model and pass it to a template.
"""

from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User


# Create your views here.
def post_list(request):
    me = User.objects.get(username="aarjav")
    posts = Post.objects.filter(author=me).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})
    # Essentially saying "Take the request and return the render of the template blog/post_list.html"
    # Syntax of render function: render(request, template_name, extras)
    # extras is a dictionary of variables to pass to the template
