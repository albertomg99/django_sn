from django import forms
from .models import AMGPost


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Post something",
                "class": "textarea is-info is-medium",
            }
        ),
        label="",
    )

    class Meta:
        model = AMGPost
        exclude = ("user",)
