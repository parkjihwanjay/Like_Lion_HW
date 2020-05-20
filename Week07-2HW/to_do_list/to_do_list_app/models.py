from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    day = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.title