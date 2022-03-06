
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def add_book_view(request, *args, **kwargs):
    return render(request, "add_book.html", {})


def add_reader_view(request, *args, **kwargs):
    return render(request, "add_reader.html", {})


def borrow_view(request, *args, **kwargs):
    return render(request, "borrow_view.html", {})


def giveback_view(request, *args, **kwargs):
    return render(request, "giveback_view.html", {})


def search_reader_view(request, *args, **kwargs):
    return render(request, "search_reader.html", {})


def search_book_view(request, *args, **kwargs):
    return render(request, "search_book.html", {})


def book_list_view(request, *args, **kwargs):
    return render(request, "book_list.html", {})   


def reader_list_view(request, *args, **kwargs):
    return render(request, "reader_list.html", {})


def book_view(request, *args, **kwargs):
    context = {
        "title": "Czerwone Drzewo I magiczne krzesło",
        "author": "Andrzej Maleszka",
        "publisher": "Czarna Owca Wydawnictwo",
        "isbn": "0922114556655426",
        "description": "Chcesz zaprzyjaźnić się z Kukim, Tosią i Filipem? Wyrusz wraz z nimi do świata magii, który nie jest zarezerwowany tylko dla dzieci. Książka „Czerwone krzesło. Magiczne drzewo” Tom 1 pozwoli Ci poznać młode osoby, które mierzą się w życiu z wieloma trudnościami. W ich pokonaniu może pomóc tytułowe krzesło, które okazuje się magiczne.",
        "insert_date": "06.03.2022",
        "borrowed": False
    }
    return render(request, 'book_view.html', context)
