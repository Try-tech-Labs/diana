from rest_framework import viewsets

from app.content.models import Post
from app.content.serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
