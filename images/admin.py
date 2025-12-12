from django.contrib import admin
from .models import Image, Comment


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['user__username', 'body']
