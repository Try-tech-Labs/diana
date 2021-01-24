from django.contrib import admin

from .models import Post, PostCategory, Tag, Tweet, Video, TwitterTrendingTopic


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "category",
        "search_count",
        "creation_date",
    )
    search_fields = ("id", "title", "category__title", "search_count", "creation_date")


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("id", "title", "description")


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    search_fields = ("id", "title")


class TwitterTrendingTopicsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "creation_date", "trends_position")
    list_filter = ("id", "title", "post__title")
    search_fields = ("id", "title", "creation_date")


class TweetAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "source", "author", "creation_date")
    list_filter = ("author", "tags")
    search_fields = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
    )


class VideoAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "source", "author", "creation_date")
    list_filter = ("author", "tags")
    search_fields = (
        "id",
        "title",
        "source",
        "author",
        "creation_date",
    )


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Tweet, TweetAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(TwitterTrendingTopic, TwitterTrendingTopicsAdmin)
