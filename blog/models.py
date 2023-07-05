from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CustomModelManager(models.Manager):
    def get_query(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    published_at = models.DateTimeField(default=timezone.now, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    objects = models.Manager()
    published_objects = CustomModelManager()

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    status = models.CharField(default=Status.DRAFT, choices=Status.choices, max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_at']


