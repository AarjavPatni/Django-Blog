from django import forms
from .models import Post


# ModelForm is the model and PostForm is the name of the form we're creating
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
        )
