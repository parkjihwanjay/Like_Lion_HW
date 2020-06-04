from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    day = models.DateField()
    time = models.TimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "posts")

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'comments')
    content = models.TextField()
    comment_date = models.TextField()

class Picture(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'pictures')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'pictures')
    content = models.TextField()