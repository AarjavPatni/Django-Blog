"""
Views request information from the model and pass it to a template.
"""

from django.shortcuts import render


# Create your views here.
def post_list(request):
    return render(request, "blog/post_list.html", {})
    # Essentially saying "Take the request and return the render of the template blog/post_list.html"
    # Syntax of render function: render(request, template_name, context)
