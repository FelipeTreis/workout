from django.contrib.auth.models import User
from django.db import models


class Workout(models.Model):

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(blank=True, default='')
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )


def __str__(self):
    return self.title
