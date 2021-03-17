from pytz import UTC as utc
from rest_framework import serializers
from rest_framework.fields import DateTimeField

from app.content.models import (
    News,
    Post,
    Tweet,
    Video,
    PostCategory,
    Tag,
    TwitterTrendingTopic,
)


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = "__all__"


class TweetsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Tweet
        fields = "__all__"


class VideosSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = Video
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)

    class Meta:
        model = News
        fields = "__all__"


class TwitterTrendingTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterTrendingTopic
        fields = "__all__"


class PostsSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer(read_only=True)
    trending_topics = TwitterTrendingTopicSerializer(read_only=True, many=True)
    creation_date = DateTimeField(default_timezone=utc)

    class Meta:
        model = Post
        fields = "__all__"
