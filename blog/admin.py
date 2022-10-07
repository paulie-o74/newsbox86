from django.contrib import admin
from .models import Category, Post, Comment


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    """
    Register the Categories model in the Admin area
    """
    list_display = ('cat_title',)
    search_fields = ['cat_title']
    prepopulated_fields = {'slug': ('cat_title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Register the Post model in the Admin area
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    actions = ['publish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status=1)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Register the Comment model in the Admin area
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
