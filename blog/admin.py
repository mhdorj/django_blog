from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published_at', 'status']
    list_filter = ['status', 'created_at', 'published_at', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {
        'slug': ['title']
    }
    ordering = ['status', 'published_at']
    raw_id_fields = ('author', )
    date_hierarchy = 'published_at'
