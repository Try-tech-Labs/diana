from rest_framework import serializers

from .models import Post
from .models import Tweet
from .models import Video
from .models import PostCategory
from .models import Tag


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = '__all__'


class TweetsSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    category = PostCategorySerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = '__all__'


class VideosSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True, many=True)
    category = PostCategorySerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class PostsSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer(read_only=True)
    videos = VideosSerializer(read_only=True, many=True)
    tweets = TweetsSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'
