from django.urls import path
from . import views  # Import the views module from the blog application

urlpatterns = [
    path("", views.post_list, name="post_list"),
    # The domain name is ignored. Tells Django to go to the views.post_list view at the domain root.
    # The name is used to identify the view.
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    # When django encounters a URL like post/5/, it will call the post_detail view with 5 as pk's value.
    path("post/new/", views.post_new, name="post_new"),
    # Syntax: path(route, view, name)
    path("post/<int:pk>/edit/", views.post_edit, name="post_edit"),
]
