from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/base_syntax', views.show_article_base_syntax, name='show_article_base_syntax'),
    path('articles/oop', views.show_article_oop, name='show_article_oop'),
    path('articles/django', views.show_article_django, name='show_article_django'),
]