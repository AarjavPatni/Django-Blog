from django.urls import path
from . import views  # Import the views module from the blog application

urlpatterns = [
    path("", views.post_list, name="post_list"),
    # The domain name is ignored. Tells Django to go to the views.post_list view at the domain root.
    # The name is used to identify the view.
]
