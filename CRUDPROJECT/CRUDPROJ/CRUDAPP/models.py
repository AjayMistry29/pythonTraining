from django.db import models

# Create your models here.
from django.urls import reverse

class Blog(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk': self.pk})
