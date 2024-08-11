from django import forms

from ..models import Post


class PostCreateForm(forms.ModelForm):
    """Post create form."""

    class Meta:
        model = Post
        fields = (
            "title",
            "content",
        )
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control w-auto"}),
            "content": forms.Textarea(attrs={"class": "form-control w-auto"}),
        }
