from rest_framework import viewsets

from .models import Post
from .serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    serializer_class = PostsSerializer
    queryset = Post.objects.all()
