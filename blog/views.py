from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Post, Categories
from .forms import PostForm


class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(generic.CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ('title', 'content', 'category', 'featured_image')


class UpdatePostView(generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})