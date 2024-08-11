import factory
from factory.django import DjangoModelFactory

from .. import models as posts_models


class PostFactory(DjangoModelFactory):
    class Meta:
        model = posts_models.Post

    author = factory.SubFactory("users.factories.UserFactory")
    title = factory.Faker("sentence")
    content = factory.Faker("sentence")
    created_at = factory.Faker("date_time")
    modified_at = factory.Faker("date_time")
    deleted_at = factory.Faker("date_time")
