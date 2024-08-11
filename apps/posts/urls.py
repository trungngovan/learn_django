from django.urls import path

from ..posts import views

urlpatterns = [
    path(
        "",
        views.PostListView.as_view(),
        name="post-list",
    ),
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post-detail",
    ),
    path(
        "posts/create/",
        views.PostCreateView.as_view(),
        name="post-create",
    ),
    # path(
    #     "posts/<int:pk>/update/",
    #     views.PostUpdateView.as_view(),
    #     name="update-post"
    # ),
    # path(
    #     "posts/<int:pk>/delete/",
    #     views.PostDeleteView.as_view(),
    #     name="delete-post"
    # ),
]
