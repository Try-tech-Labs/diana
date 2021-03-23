from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=280)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class PostCategory(BaseModel):
    description = models.CharField(max_length=255)


class Post(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    search_count = models.PositiveIntegerField(default=0)


class TwitterTrendingTopic(BaseModel):
    trends_position = models.IntegerField()
    post = models.ForeignKey(
        to=Post, on_delete=models.CASCADE, related_name="trending_topics", null=True
    )


class Tag(BaseModel):
    twitter_trending_topic = models.ForeignKey(
        to=TwitterTrendingTopic,
        on_delete=models.CASCADE,
        related_name="tags",
        null=True,
    )


class BaseContentModel(BaseModel):
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    source_url = models.URLField()

    class Meta:
        abstract = True


class Video(BaseContentModel):
    trending_topic = models.ForeignKey(
        to=TwitterTrendingTopic,
        on_delete=models.CASCADE,
        related_name="videos",
        null=True,
    )
    length = models.FloatField()
    content = models.TextField(max_length=512)


class Tweet(BaseContentModel):
    trending_topic = models.ForeignKey(
        to=TwitterTrendingTopic,
        on_delete=models.CASCADE,
        related_name="tweets",
        null=True,
    )
    content = models.TextField(max_length=280)


class News(BaseContentModel):
    trending_topic = models.ForeignKey(
        to=TwitterTrendingTopic,
        on_delete=models.CASCADE,
        related_name="news",
        null=True,
    )
    thumbnail = models.URLField()
    content = models.CharField(max_length=512)
