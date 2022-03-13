from symtable import Class
from django import forms
import datetime
from .models import book

class BookForm(forms.ModelForm):
    title = forms.CharField(
        label=(''),
        widget=forms.TextInput(attrs={"placeholder": "Tytuł: " ,'class':'form_input'}),
        required=True,
    )

    author = forms.CharField(
    label=(''),
    widget=forms.TextInput(attrs={"placeholder": "Autor: ", 'class':'form_input'}),
    required=True,
    )

    publisher = forms.CharField(

        label=(''),
        widget=forms.TextInput(attrs={"placeholder": "Wydawca: ",'class':'form_input'}),
        required=False,
    )

    ISBN = forms.CharField(
        label=(''),
        widget=forms.TextInput(attrs={"placeholder": "ISBN: " ,'class':'form_input'}),
        required=False,
    )
    
    description = forms.CharField(
        label=(''),
        widget=forms.Textarea(attrs={"placeholder": "Opis: " ,'class':'form_input'}),
        required=False,
    )

    insert_date = forms.DateField(
        initial=datetime.date.today,
        label=(''),
        required=False,
    )

    volume = forms.IntegerField(
        label=(''),
        widget=forms.NumberInput(attrs={"placeholder": "Numer Tomu: "}),
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
