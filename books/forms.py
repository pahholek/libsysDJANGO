from django import forms
import datetime
from .models import book

class BookForm(forms.ModelForm):
    title = forms.CharField(
        label=('Tytuł'),
        widget=forms.TextInput(attrs={"placeholder": "Wpisz Tytuł"}),
        required=True,
    )

    author = forms.CharField(
    label=('Autor'),
    widget=forms.TextInput(attrs={"placeholder": "Podaj Autora"}),
    required=True,
    )

    publisher = forms.CharField(
        label=('Wydawca'),
        widget=forms.TextInput(attrs={"placeholder": "Podaj Wydawce"}),
        required=False,
    )

    ISBN = forms.CharField(
        label=('ISBN'),
        widget=forms.TextInput(attrs={"placeholder": "Podaj ISBN"}),
        required=False,
    )
    
    description = forms.CharField(
        label=('Opis'),
        widget=forms.Textarea(attrs={"placeholder": "Podaj Opis"}),
        required=False,
    )

    insert_date = forms.DateField(
        initial=datetime.date.today,
        label=('Data Wprowadzenia'),
        required=False,
    )

    volume = forms.IntegerField(
        label=('Numer Tomu'),
        widget=forms.NumberInput(attrs={"placeholder": "Podaj Number Tomu"}),
        required=False,
    )
    class Meta:
        model = book
        fields = [
            'title',
            'author',
            'publisher',
            'ISBN',
            'description',
            'insert_date',
            'volume',
        ]
