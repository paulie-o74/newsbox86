from django.contrib import admin
from .models import Post, Categories, Comment

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(Comment)