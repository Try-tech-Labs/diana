import pytest
from collections import OrderedDict

from app.content.tests.factories import (
    PostFactory,
    TwitterTrendingTopicFactory,
    VideoFactory,
    NewsFactory,
    TweetsFactory,
)
from app.content.serializers import (
    PostsSerializer,
    TwitterTrendingTopicSerializer,
    VideosSerializer,
    NewsSerializer,
    TweetsSerializer,
)


class TestPostSerializer:
    @pytest.fixture
    def post(self):
        return PostFactory()

    def test_it_returns_the_expected_values(self, post):
        data = PostsSerializer(post).data
        expected_post = {
            "category": OrderedDict(
                [
                    ("id", post.category.id),
                    ("title", post.category.title),
                    (
                        "creation_date",
                        post.category.creation_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    ),
                    ("description", post.category.description),
                ]
            ),
            "trending_topics": [],
            "creation_date": post.creation_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "id": post.id,
            "search_count": post.search_count,
        }
        assert data == expected_post


class TestTwitterTrendingTopicSerializer:
    @pytest.fixture
    def trending_topic(self):
        return TwitterTrendingTopicFactory()

    def test_it_returns_the_expected_values(self, trending_topic):
        data = TwitterTrendingTopicSerializer(trending_topic).data
        print(data)
        expected_trending_topic = {
            "post": None,
            "trends_position": 1,
            "title": "Godzilla vs. Kong",
            "creation_date": trending_topic.creation_date.strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ),
            "id": None,
        }

        assert data == expected_trending_topic


class TestVideoSerializer:
    @pytest.fixture
    def video(self):
        return VideoFactory()

    def test_it_returns_the_expected_values(self, video):
        data = VideosSerializer(video).data
        expected_video = {
            "id": None,
            "trending_topic": None,
            "length": 10.5,
            "content": "Test video content",
            "author": "UOL",
            "source": "Youtube",
            "source_url": "https://youtube.com",
            "creation_date": video.creation_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "title": "Test video",
        }
        assert data == expected_video


class TestNewsSerializer:
    @pytest.fixture
    def news(self):
        return NewsFactory()

    def test_it_returns_the_expected_values(self, news):
        data = NewsSerializer(news).data
        expected_news = {
            "id": None,
            "trending_topic": None,
            "thumbnail": "https://images.com",
            "content": "Test news content",
            "author": "BBC",
            "source": "source",
            "source_url": "https://www.bbc.com/",
            "creation_date": news.creation_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "title": "Test news",
        }
        assert data == expected_news


class TestTweetsSerializer:
    @pytest.fixture
    def tweets(self):
        return TweetsFactory()

    def test_it_returns_the_expected_values(self, tweets):
        data = TweetsSerializer(tweets).data
        expected_tweets = {
            "id": None,
            "trending_topic": None,
            "content": "Test tweets content",
            "author": "Clayton Veras",
            "source": "@Clayton_veras",
            "source_url": "https://twitter.com/Clayton_veras",
            "creation_date": tweets.creation_date.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "title": "Test Tweet",
        }
        assert data == expected_tweets
