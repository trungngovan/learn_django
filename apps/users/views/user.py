from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy

from ..forms import UserLoginForm, UserSignupForm


class UserLoginView(LoginView):
    """Provide user login page.

    This page will redirect to the home page if the user is already
    authenticated.

    """

    template_name = "users/auth/login.html"
    authentication_form = UserLoginForm
    redirect_authenticated_user = True
    next_page = reverse_lazy("post-list")


class UserLogoutView(LogoutView):
    """Logout user and redirect to login page."""

    next_page = reverse_lazy("user-login")


class UserSignupView(CreateView):
    """User create view."""

    form_class = UserSignupForm
    template_name = "users/auth/signup.html"
    success_url = reverse_lazy("user-login")
