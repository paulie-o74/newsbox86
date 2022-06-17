from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=200, default='coding')
    featured_image = CloudinaryField('image', default='placeholder')
    # slug = models.SlugField(max_length=200, unique=True, null=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                     related_name="submitted_by")
    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"{self.title}"

    # def get_absolute_url(self):
    #     # return reverse('post_detail', args=(str(self.slug)))
    #     return reverse('home')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)