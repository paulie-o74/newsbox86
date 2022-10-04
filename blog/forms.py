from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    """
    Class to enable data entry and collection via
    comment form with body field included
    """
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    """
    All details of the post form
    """
    class Meta:
        model = Post
        exclude = ('author', 'slug', 'likes', 'updated_on', 'excerpt', 'status')
