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
