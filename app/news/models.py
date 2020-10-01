from django.db import models


class BaseModel(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class PostCategory(BaseModel):
    description = models.CharField(max_length=255)


class PostMetaModel(models.Model):
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    search_count = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        abstract = True


class Post(BaseModel, PostMetaModel):
    pass


class Tag(BaseModel):
    pass


class BaseContentModel(BaseModel):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    source = models.CharField(max_length=255)
    source_url = models.URLField()
    tags = models.ManyToManyField(Tag)

    class Meta:
        abstract = True


class Video(PostMetaModel, BaseContentModel):
    length = models.IntegerField()


class Tweet(PostMetaModel, BaseContentModel):
    author = models.CharField(max_length=255)
