# Importing specific modules from django.db, django.utils, and django.conf
from django.db import models
from django.utils import timezone
from django.conf import settings


# Django models are basically objects that represent your data in the database.
# Create your models here.
class Post(models.Model):  # Post is a type of Model and inherits properties.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # ForeignKey - link to another model.
    title = models.CharField(
        max_length=200
    )  # CharField - field for small to large strings.
    text = models.TextField()  # TextField is a field for large text.
    created_date = models.DateTimeField(
        default=timezone.now
    )  # DateTimeField - field for date and time.
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # The self keyword tells python to automatically pass the instance as the argument to the method.
    # In this case, the publish method sets the published_date of the current instance to the current date and time.

    # __str__ method is a method that returns a string representation when we try to print the object's instance.
    def __str__(self):
        return self.title
