from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'search_count', 'creation_date')
    search_fields = ('id', 'title', 'category__title', 'search_count', 'creation_date')


admin.site.register(Post, PostAdmin)
