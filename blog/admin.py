from django.contrib import admin
from .models import Author, Category, Post, Comment

admin.site.register(Author)


@admin.register(Category)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['cat_title']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('timestamp', 'author', 'likes')
    list_display = ('title', 'timestamp')
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'approved')
    list_display = ('name', 'created_on', 'post', 'body', 'approved')
    search_fields = ['post', 'post', 'name', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
