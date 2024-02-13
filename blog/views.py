"""
Views request information from the model and pass it to a template.
"""

from django.shortcuts import render
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "blog/post_list.html", {"posts": posts})
    # Essentially saying "Take the request and return the render of the template blog/post_list.html"
    # Syntax of render function: render(request, template_name, extras)
    # extras is a dictionary of variables to pass to the template
