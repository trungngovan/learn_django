from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from ..models import User


class UserLoginForm(AuthenticationForm):
    """Custom login form."""

    # Overriding username as email for authentication
    username = forms.EmailField(
        label=_("Email"),
        widget=forms.EmailInput(
            attrs={
                "placeholder": _("Email"),
                "class": "form-control",
                "autofocus": True,
            },
        ),
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Password"),
                "class": "form-control",
            },
        ),
    )

    class Meta:
        model = User
        field = ("username", "password")


class UserSignupForm(forms.ModelForm):
    """Form for creating new users."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
        )
        widgets = {
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First name",
                },
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last name",
                },
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email address",
                },
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Password",
                },
            ),
        }

    def save(self, commit: bool = True) -> User:
        """Save the provided password in hashed format."""
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user
