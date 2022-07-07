from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .utils import DataMixin
from .forms import ReviewForm, AddForm


# Create your views here.

class HomeView(DataMixin, ListView):
    template_name = 'book/main.html'
    extra_context = {'title': 'Библиотека'}

    def get_queryset(self):
        return Book.objects.all().select_related('category')


class BookDetailView(DataMixin, DetailView):
    template_name = 'book/book_info.html'
    slug_url_kwarg = 'book_slug'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['books'].title)
        return context

    def get_queryset(self):
        return Book.objects.filter(slug=self.kwargs['book_slug'])


class CategoryInfoView(DataMixin, ListView):
    template_name = 'book/books_for_category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = Category.objects.get(slug=self.kwargs['category_slug'])
        context['title'] = str(cat.name)
        return context

    def get_queryset(self):
        return Book.objects.filter(category__slug=self.kwargs['category_slug'])


class AddReview(View):

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)
        user = User.objects.get(username=request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.book = book
            form.user = user
            form.save()
        return redirect(book.get_absolute_url())


class AddCrateView(CreateView):
    model = Book
    template_name = 'book/add_book.html'
    form_class = AddForm
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddCrateView, self).form_valid(form)


class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book/add_book.html'
    form_class = AddForm
    success_url = '/'

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        return queryset


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book/delete_book.html'
    success_url = '/'

    def get_queryset(self):
        queryset = Book.objects.filter(user=self.request.user)
        print(queryset)
        return queryset






