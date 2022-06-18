# from allauth.account.forms import SignupForm
from django import forms
from .models import Post, Categories, Comment

# Autopopulate the categories dropdown menu

CHOICES = Categories.objects.all().values_list('cat_title', 'cat_title')

CHOICE_LIST = []

for item in CHOICES:
    CHOICE_LIST.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'featured_image',\
                  'submitted_by')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'submitted_by': forms.TextInput(
                attrs={'class': 'form-control',
                       'value': '', 'id': 'elder', 'type': 'hidden'}),
            'category': forms.Select(choices=CHOICE_LIST,
                                     attrs={'class': 'form-control'})
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
            }
