from django.urls import path

from . import views

urlpatterns = [
    path(
        "login/",
        view=views.UserLoginView.as_view(),
        name="user-login",
    ),
    path(
        "logout/",
        view=views.UserLogoutView.as_view(),
        name="user-logout",
    ),
    path(
        "signup/",
        view=views.UserSignupView.as_view(),
        name="user-signup",
    ),
]
