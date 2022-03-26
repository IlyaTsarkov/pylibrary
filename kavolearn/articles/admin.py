from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


# Register your models here.
class ArticlesAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Articles, ArticlesAdmin)
admin.site.register(ArticlesCategories)
admin.site.register(ArticlesCategoriesMini)
