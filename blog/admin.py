from django.contrib import admin
from .models import Post, Categories, Comment

# Register models on the admin

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('category', 'created_on', 'updated_on', 'submitted_by')
    list_display = ('title', 'created_on', 'updated_on')
    search_fields = ['title', 'content', 'submitted_by']


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_filter = ('created_on',)
    list_display = ('cat_title', 'created_on')
    search_fields = ['cat_title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'comment_author')
    list_display = ('comment_author', 'created_on', 'post')
    search_fields = ['comment', 'post', 'comment_author']
