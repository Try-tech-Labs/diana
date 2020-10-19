from django.db import models
from django.utils import timezone


class BaseModel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class PostCategory(BaseModel):
    description = models.CharField(max_length=255)


class Post(BaseModel):
    category = models.ForeignKey(to=PostCategory, on_delete=models.CASCADE)
    search_count = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
