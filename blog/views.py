from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic, View
from .models import Post, Categories
from .forms import PostForm
from django.http import HttpResponseRedirect


class HomeView(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 8


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()

        info = get_object_or_404(Post, id=self.kwargs['pk'])
        total_up_votes = info.total_up_votes()

        up_voted = False
        if info.up_votes.filter(id=self.request.user.id).exists():
            up_voted = False

        context["total_up_votes"] = total_up_votes
        context["up_voted"] = up_voted
        return context


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
    category_posts = Post.objects.filter(category=cats).order_by('-created_on')
    return render(request, 'categories.html', {'cats': cats.title(), 'category_posts': category_posts})


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    up_voted = False
    if post.up_votes.filter(id=request.user.id).exists():
        post.up_votes.remove(request.user)
        up_voted = False
    else:
        post.up_votes.add(request.user)
        up_voted = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))