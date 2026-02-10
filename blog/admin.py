from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ('body',)


admin.site.register(Comment, CommentAdmin)
