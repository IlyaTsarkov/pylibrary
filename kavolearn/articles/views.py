from django.shortcuts import render
from .models import Articles


# Create your views here.
def show_article_base_syntax(request):
    return render(request, 'articles/show_article_base_syntax.html')


def show_article_oop(request):
    return render(request, 'articles/show_article_oop.html')


def show_article_django(request):
    return render(request, 'articles/show_article_django.html')
