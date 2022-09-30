from django.contrib.auth import get_user_model
from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone


User = get_user_model()


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = CloudinaryField()
	
    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = CloudinaryField('image', default='placeholder')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
    likes = models.ManyToManyField(Author, related_name='likes')

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Comment Model
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"























# from django.db import models
# from django.contrib.auth.models import User
# from django.urls import reverse
# from django.utils import timezone
# from cloudinary.models import CloudinaryField


# class Categories(models.Model):
#     cat_title = models.CharField(max_length=200, unique=True)
#     cat_featured_image = CloudinaryField('image', default='placeholder')
#     created_on = models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering = ['created_on']
#         verbose_name = "Categories"
#         verbose_name_plural = "Categories"

#     def __str__(self):
#         return f"{self.cat_title}"

#     def get_absolute_url(self):
#         return reverse('home')


# class Post(models.Model):
#     title = models.CharField(max_length=200, unique=True)
#     content = models.TextField()
#     category = models.CharField(max_length=200,
#                                 default='Choose from this dropdown list')
#     featured_image = CloudinaryField('image', default='placeholder')
#     submitted_by = models.ForeignKey(User, on_delete=models.CASCADE,
#                                      related_name="submitted_by")
#     created_on = models.DateTimeField(default=timezone.now)
#     updated_on = models.DateTimeField(default=timezone.now)
#     up_votes = models.ManyToManyField(User, related_name='up_votes')

#     class Meta:
#         ordering = ['created_on']

#     def total_up_votes(self):
#         return self.up_votes.count()

#     def __str__(self):
#         return f"{self.title}"

#     def get_absolute_url(self):
#         # return reverse('post_detail', args=(str(self.pk)))
#         return reverse('index')


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, 
#                              related_name="comments")
#     comment_author = models.CharField(max_length=80)
#     comment = models.TextField()
#     created_on = models.DateTimeField(default=timezone.now)

#     class Meta:
#         ordering = ['-created_on']

#     def __str__(self):
#         return f"Comment {self.comment} by {self.comment_author}"
