from django.contrib import admin

from app.content.models import (
    News,
    Post,
    PostCategory,
    Tag,
    Tweet,
    Video,
    TwitterTrendingTopic,
)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "category",
        "search_count",
        "creation_date",
    )
    search_fields = ("id", "category__title", "search_count", "creation_date")


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("id", "title", "description")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "twitter_trending_topic")
    search_fields = ("id", "title")


class TwitterTrendingTopicsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creation_date", "trends_position", "post")
    list_filter = ("id", "title", "creation_date")
    search_fields = ("id", "title", "creation_date", "post__creation_date")


class TweetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
        "source_url",
        "trending_topic",
        "content",
    )
    list_filter = ("author", "creation_date")
    search_fields = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
        "tending_topic__title",
    )


class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "content",
        "source",
        "author",
        "creation_date",
        "trending_topic",
        "thumbnail",
    )
    list_filter = ("author", "creation_date")
    search_fields = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
        "tending_topic__title",
    )


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
        "length",
        "trending_topic",
    )
    list_filter = ("author", "creation_date")
    search_fields = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
        "tending_topic__title",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(TwitterTrendingTopic, TwitterTrendingTopicsAdmin)
