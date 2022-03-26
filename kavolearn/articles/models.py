from django.db import models


# Create your models here.
class Articles(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True, null=True)
    posted = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.title


class ArticlesCategories(models.Model):
    categories_title = models.CharField(max_length=250, blank=True, null=True),
    categories = models.ForeignKey(Articles, on_delete=models.PROTECT, null=True)


class ArticlesCategoriesMini(models.Model):
    categories_mini_title = models.CharField(max_length=250, blank=True, null=True)
    categories_mini = models.ForeignKey(ArticlesCategories, on_delete=models.PROTECT, null=True)
