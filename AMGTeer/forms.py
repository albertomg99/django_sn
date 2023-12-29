from django import forms
from django.contrib.auth.forms import UserCreationForm
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


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields
