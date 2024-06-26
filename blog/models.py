# blog/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    email = models.EmailField(default='default@example.com')
    content = models.TextField(max_length=100, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


# Create your models here.
