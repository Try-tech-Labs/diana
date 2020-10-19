from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class PostCategory(BaseModel):
    description = models.CharField(max_length=255)


class PostMetaModel(models.Model):
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    search_count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class Post(BaseModel, PostMetaModel):
    pass


class Tag(BaseModel):
    pass


class Tweet(BaseModel, PostMetaModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=255)
    tags = models.ManyToManyField(Tag)
    source = models.CharField(max_length=255)
    source_url = models.URLField()
