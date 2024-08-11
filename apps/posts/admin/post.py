from django.contrib import admin

from .. import models as posts_models


@admin.register(posts_models.Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ("-created_at",)
    list_display = (
        "id",
        "author",
        "title",
        "content",
        "created_at",
        "modified_at",
        "deleted_at",
    )

    list_display_links = (
        "id",
        "title",
    )

    list_filter = (
        "author",
    )

    search_fields = (
        "author",
        "title",
        "content",
    )

    fieldsets = (
        ("Post", {
            "fields": (
                "author",
                "title",
                "content",
            ),
        }),
    )
