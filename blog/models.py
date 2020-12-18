from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField(default="")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_read_detail', args=[str(self.id)])
    
    # allows to alter singula and plural naming of model
    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
