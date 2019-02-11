from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):

    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Tag(models.Model):

    tag_name = models.CharField(max_length=70)

    def __str__(self):
        return self.tag_name


class Post(models.Model):

    title = models.CharField(max_length=100)

    body = models.TextField()

    create_date = models.DateTimeField(auto_now=True)

    modified_date = models.DateTimeField(auto_now=True)

    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=True)

    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=True)

    def get_absolute_url(self):

        # reverse 函数，它的第一个参数的值是 'Documents:detail'，意思是 Documents 应用下的 name=detail 的函数
        return reverse('Documents:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
