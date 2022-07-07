from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField


# Create your models here.
class CustomManager(models.Manager):
    def year_gte(self):
        return super().get_queryset().filter(year__gte=2000)


class Category(models.Model):
    name = models.CharField(max_length=150, null=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True, null=True)

    def get_absolute_url(self):
        return reverse('category_info', kwargs={'category_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']


class Author(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True, null=True)
    description = RichTextField()
    year = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    authors = models.ManyToManyField(Author, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('book_info', kwargs={'book_slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

    objects = models.Manager()
    custom_manager = CustomManager()


class Review(models.Model):
    content = models.TextField(max_length=3000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"отзыв к {self.book}"


class Test(models.Model):
    name = models.CharField(blank=True, max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)


