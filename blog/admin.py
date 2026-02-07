from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title', 'content')


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('body',)


admin.site.register(Comment, CommentAdmin)
