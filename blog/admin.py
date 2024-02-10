from django.contrib import admin
from .models import Post

admin.site.register(Post)
# What does this do?
# The code registers the Post model with the admin site.
# Registering means that the Post model will be visible on the admin site.
