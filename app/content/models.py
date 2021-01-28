from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class BaseModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=280)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class PostCategory(BaseModel):
    description = models.CharField(max_length=255)


class TwitterTrendingTopic(BaseModel):
    trends_position = models.IntegerField()
    post = models.ForeignKey(
        to="content.Post", on_delete=models.CASCADE, related_name="trending_topics"
    )


class Post(BaseModel):
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    search_count = models.PositiveIntegerField(default=0)


class Tag(BaseModel):
    pass


class BaseContentModel(BaseModel):
    author = models.CharField(max_length=255)
    source = models.CharField(max_length=255)
    source_url = models.URLField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True


class Video(BaseContentModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="videos")
    length = models.FloatField()
    content = models.TextField(max_length=512)


class Tweet(BaseContentModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(max_length=280)


class News(BaseContentModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name="news")
    thumbnail = models.URLField()
    content = models.CharField(max_length=512)
