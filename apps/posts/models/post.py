from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.users.models import User
from ..querysets import PostQuerySet


class PostManager(models.Manager):
    """Custom manager for Post model."""

    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


class Post(models.Model):
    """ Represent a post model. """

    author = models.ForeignKey(
        User,
        verbose_name=_("Author"),
        on_delete=models.PROTECT,
    )

    title = models.CharField(
        verbose_name=_("Title"),
        max_length=255,
    )

    content = models.TextField(
        verbose_name=_("Content"),
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

    objects = PostManager()
