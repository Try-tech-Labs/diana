import factory

from datetime import datetime
from pytz import UTC as utc
from app.content.models import (
    Tag,
    Post,
    PostCategory,
    TwitterTrendingTopic,
    Video,
    News,
    Tweet,
)


class CategoryFactory(factory.Factory):
    class Meta:
        model = PostCategory

    title = "Entertainment"
    description = """
    A form of activity that holds the attention
    and interest of an audience or gives pleasure and delight.
    """
    creation_date = datetime.now(tz=utc)


class PostFactory(factory.Factory):
    class Meta:
        model = Post

    category = factory.SubFactory(CategoryFactory)
    search_count = 1
    creation_date = datetime.now(tz=utc)


class TagFactory(factory.Factory):
    class Meta:
        model = Tag

    title = "Movies"
    creation_date = datetime.now(tz=utc)


class TwitterTrendingTopicFactory(factory.Factory):
    class Meta:
        model = TwitterTrendingTopic

    trends_position = 1
    post = factory.SubFactory(PostFactory)
    title = "Godzilla vs. Kong"
    creation_date = datetime.now(tz=utc)


class VideoFactory(factory.Factory):
    class Meta:
        model = Video

    trending_topic = factory.SubFactory(TwitterTrendingTopicFactory)
    length = 10.5
    content = "Test video content"
    author = "UOL"
    source = "Youtube"
    source_url = "https://youtube.com"
    title = "Test video"
    creation_date = datetime.now(tz=utc)


class NewsFactory(factory.Factory):
    class Meta:
        model = News

    trending_topic = factory.SubFactory(TwitterTrendingTopicFactory)
    thumbnail = "https://images.com"
    content = "Test news content"
    author = "BBC"
    source = "source"
    source_url = "https://www.bbc.com/"
    title = "Test news"
    creation_date = datetime.now(tz=utc)


class TweetsFactory(factory.Factory):
    class Meta:
        model = Tweet

    trending_topic = factory.SubFactory(TwitterTrendingTopicFactory)
    content = "Test tweets content"
    author = "Clayton Veras"
    source = "@Clayton_veras"
    source_url = "https://twitter.com/Clayton_veras"
    title = "Test Tweet"
    creation_date = datetime.now(tz=utc)
