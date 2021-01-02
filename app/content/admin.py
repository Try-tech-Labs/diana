from django.contrib import admin

from .models import Post
from .models import PostCategory
from .models import Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'search_count', 'creation_date')
    search_fields = ('id', 'title', 'category__title', 'search_count', 'creation_date')


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'description')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Tag, TagAdmin)
