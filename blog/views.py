from django.shortcuts import render
from django.views import generic, View
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

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
    template_name = 'add_post.html'
    fields = '__all__'
