from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from ..forms import PostCreateForm
from ..models import Post


class PostListView(LoginRequiredMixin, ListView):
    """Post list view."""

    model = Post
    paginate_by = 10
    template_name = "posts/post_list.html"
    context_object_name = "posts"
    queryset = Post.objects.all().order_by(
        "title",
        "-created_at",
    )

    def get_queryset(self):
        """Return only available courses for current user."""
        return super().get_queryset().available_for_user(
            self.request.user,
        )

    def get_login_url(self) -> str:
        """Redirect to implemented login url instead of default one."""
        return reverse_lazy("login")


class PostDetailView(LoginRequiredMixin, DetailView):
    """Post detail view."""

    model = Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    """Post create view."""

    form_class = PostCreateForm
    template_name = "posts/post_create.html"
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
