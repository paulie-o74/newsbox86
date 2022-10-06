from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.text import slugify
from .models import Post, Comment, Category
from .forms import CommentForm, PostForm, PostSearchForm


class PostList(generic.ListView):
    """
    Post List Class Based View for displaying current post
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    """
    Post Detail Class Based View for displaying selected post's detail
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        category = post.category
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "category": category,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Post method to add comments and likes
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )



class PostLike(View):
    """
    Post Like Class Based View for managing the like an unlike actions
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_post(request):
    """ Add a post to the blog """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            form.save()
            messages.success(request, 'Successfully added post for review.')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Failed to add post. \
                           Please ensure the form is valid.')
    else:
        form = PostForm()

    template = 'add_post.html',
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_post(request, slug):

    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.slug = slugify(post.title)
                post.status = 1
                form.save()
                messages.success(request, 'Successfully updated post!')
                return redirect(reverse('home'))
            else:
                messages.error(request, 'Failed to update post. \
                    Please ensure the form is valid.')
        else:
            form = PostForm(instance=post)
    else:
        messages.error(request, 'Sorry. \
                    You are not authorised to perform that operaiton.')

    template = 'edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, slug):
    """ Delete a post from the blog """

    post = get_object_or_404(Post, slug=slug)
    if request.user.id == post.author.id:
        post.delete()
        messages.success(request, 'Post deleted!')
        return redirect(reverse('home'))
    else:
        messages.error(request, 'Sorry. \
            You are not authorised to perform that operaiton.')


@login_required
def delete_comment(request, pk):
    """ Delete a comment in the blog """
    Comment.objects.get(pk=pk).delete()
    messages.success(request, 'Comment deleted!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class CatListView(generic.ListView):
    """
    Category List Class Based View for displaying categories
    """
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__cat_title=self.kwargs['category']).filter(status=1)
        }
        return content


def category_list(request):
    """ Return a list of categories for the dropdown in the nav """
    category_list = Category.objects.all()
    context = {
        "category_list": category_list,
    }
    return context


def post_search(request):
    """ Return a list of posts from a search term in the nav """
    form = PostSearchForm()
    q = ''
    results = []

    if 'q' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

    return render(request, 'search.html', {
        'form': form,
        'q': q,
        'results': results
    })
