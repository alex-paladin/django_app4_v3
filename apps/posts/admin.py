from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'status']
    list_filter = ['title', 'author', 'created_at']
    search_fields = ['title', 'text']
    actions = ['make_published']


    def make_published(self, request, queryset):
        queryset.update(status='p')

    make_published.short_description = "Mark selected post as published"

admin.site.register(Post, PostAdmin)