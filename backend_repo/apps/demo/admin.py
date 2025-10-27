from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'timestamp')
    search_fields = ('text', 'user__username')
    list_filter = ('timestamp',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'user', 'post', 'timestamp')
    search_fields = ('text', 'user__username', 'post__text')
    list_filter = ('timestamp',)
