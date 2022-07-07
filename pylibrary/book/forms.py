from django import forms
from .models import *

from allauth.account.forms import LoginForm


class MyCustomLoginForm(LoginForm):
    error_messages = {
        "account_inactive": "Этот аккаунт заблокирован",
        "email_password_mismatch":
            "Неверный email или пароль"
        ,
        "username_password_mismatch":
            "Неверный логин или пароль",
    }

    def login(self, *args, **kwargs):
        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('content', )


class AddForm(forms.ModelForm):

    title = forms.CharField(label='Название', widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    description = forms.CharField(label='Описание (поддерживает html разметку)', widget=forms.Textarea(
        attrs={'class': 'form-control'}))

    year = forms.IntegerField(label='Год', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))

    category = forms.ModelChoiceField(
            queryset=Category.objects.all(),
            label='Категория',
            widget=forms.Select(attrs={'class': 'form-control'})
    )

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        label='Авторы (зажмите ctrl для множественного выбора)',
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Book
        fields = ('title', 'description', 'year', 'category', 'authors')

