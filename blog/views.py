from django.shortcuts import render
from django.views import generic, View
from .models import Post

# def home(request):
#     return render(request, 'home.html', {})

class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 8
