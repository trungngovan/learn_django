from typing import Self

from django.db import models

from apps.users.models import User


class PostQuerySet(models.QuerySet):
    """Queryset class for `Course` model."""

    def available_for_user(self, user: User) -> Self:
        """Filter available `Course` instances for provided user.

        User has access to course if they have access to any
        lecture inside the course.

        """
        if user.is_anonymous:
            return self.none()

        if user.is_staff or user.is_superuser:
            return self

        return self.filter(
            models.Q(author=user),
        ).distinct()
