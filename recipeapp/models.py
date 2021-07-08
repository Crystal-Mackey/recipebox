from django.db import models
from django.utils import timezone
# Create your models here.
"""
Author:
- name
- byline

Recipe:
- body
- author???
- post_created
- title

"""

class Author(models.Model):
    name = models.CharField(max_length=50)
    Bio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=20, blank=True, null=True)
    recipe_instructions = models.TextField(max_length=5000, blank=True, null=True)
    post_created = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title