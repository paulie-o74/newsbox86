# from allauth.account.forms import SignupForm
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'featured_image', 'submitted_by')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'submitted_by': forms.Select(attrs={'class': 'form-control', 'value': '', 'id': 'elder', 'type': 'hidden'}),
            # 'featured_image': forms.ImageField(attrs={'class': 'form-control'})
            }
