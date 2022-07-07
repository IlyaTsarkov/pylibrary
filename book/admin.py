from django.contrib import admin
from django import forms
from .models import Category, Book, Author, Review
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.
class BookAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Book
        fields = '__all__'


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    filter_horizontal = ('authors',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Review)
