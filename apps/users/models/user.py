from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import citext


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str | None = None,
        **extra_fields,
    ) -> "User":
        """Create superuser instance (used by `createsuperuser` cmd)."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=30,
        blank=True,
        validators=[
            MinLengthValidator(
                2,
                _("First name must be at least 2 characters long."),
            ),
        ],
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=30,
        blank=True,
        validators=[
            MinLengthValidator(
                2,
                _("Last name must be at least 2 characters long."),
            ),
        ],
    )
    email = citext.CIEmailField(
        verbose_name=_("Email address"),
        max_length=254,  # to be compliant with RFCs 3696 and 5321
        unique=True,
    )
    is_staff = models.BooleanField(
        verbose_name=_("Staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
    )
    is_active = models.BooleanField(
        verbose_name=_("Active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active.",
        ),
    )
    is_superuser = models.BooleanField(
        verbose_name=_("Superuser"),
        default=False,
        help_text=_("Designates that this user has all permissions."),
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created at"),
        auto_now_add=True,
    )
    modified_at = models.DateTimeField(
        verbose_name=_("Modified at"),
        auto_now=True,
    )
    deleted_at = models.DateTimeField(
        verbose_name=_("Deleted at"),
        null=True,
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self) -> str:
        return self.email
