import pytest

from django.urls import reverse

from app.content.tests.factories import PostFactory
from app.content.models import Post


class TestPostsViewSet:
    @pytest.fixture
    def posts(self):
        return PostFactory.create_batch(3)

    @pytest.fixture
    def url(self):
        return reverse("posts-list")

    def test_it_returns_a_list_of_posts(self, posts, url, admin_client):
        response = admin_client.get(url).json()
        posts = Post.objects.all()
        for item in response:
            post_id = item["id"]
            post = posts.get(id=post_id)
            assert item["search_count"] == post.search_count
            assert item["category"]["description"] == post.category.description
            assert item["creation_date"] == post.creation_date
