from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField



Status = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    excerpt = models.CharField(max_length=200, default='')
    content = SummernoteTextField()
    featured_image = models.ImageField(upload_to='featured_images/', default='placeholder')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=Status, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    number_of_likes = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"The title of this post is {self.title} | written by {self.author}"
    
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    excerpt = models.CharField(max_length=200, default='', blank=True)


    class Meta:
        ordering = ["created_on"]
        
    def __str__(self):
        return f"Comment {self.body} by {self.author}"