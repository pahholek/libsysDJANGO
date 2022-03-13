
import imp
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from books.models import book
from books.forms import BookForm
from pages.karoImport import get_data

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def add_book_view(request, *args, **kwargs):
    if request.user.is_superuser:
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('form/success')
        context = {
            'form': form,
        }

        return render(request, "add_book.html", context)
    else:
        return render(request, "no_permissions.html", {})

def add_book_isbn(request, *args, **kwargs):
    if request.user.is_superuser:
        # *!!! data is flowing through but !TODO: redirect and insert data given
        context={}
        def get_data(isbn, lib): #lib = BN - Biblioteka Narodowa, UJ - Biblioteka jagielońska
            import requests
            isbn = str(isbn)
            lib = str(lib)
            payload = {
                'kl': '',
                'al': '',
                'priority': '1',
                'uid': '',
                'dist': '2',
                'lok': 'all',
                'liczba': '5',
                'pubyearh': '',
                'pubyearl': '',
                'lang': 'pl',
                'bib': lib,
                'si': '1',
                'qt': 'F',
                'di': 'i' + isbn,
                'pp': '1',
                'detail': '3',
                'pm': 'm',
                'st1': 'ie' + isbn,
            }

            r = requests.get('https://karo.umk.pl/K_3.02/Exec/z2w_f.pl', params=payload)
            html = r.text
            print(r.url)
            from bs4 import BeautifulSoup

            soup = BeautifulSoup(html, 'lxml')
            soup.find('table', {'class': 'fulltbl'})
            table_data = [[cell.text for cell in row("td")]
                        for row in soup("tr")]
            table_size = len(table_data)
            table_data_clean = []
            # junk off
            for i in range(table_size):
                try:
                    int(table_data[i][0])
                    table_data_clean.append(table_data[i])
                except:
                    pass

            print(table_data)
            # check if data is present
            table_data_trimmed = []
            if not table_data_clean:
                return 'No_Data'
            else:
                # trim data
                for i in range(len(table_data_clean)):
                        # ISBN 0
                    if int(table_data_clean[i][0]) == 20:
                        table_data_trimmed.append(table_data_clean[i])
                        # TITLE 1
                    if int(table_data_clean[i][0]) == 245:
                        table_data_trimmed.append(table_data_clean[i])
                        # PUBLISHER 2
                    if int(table_data_clean[i][0]) == 260:
                        table_data_trimmed.append(table_data_clean[i])
                        # TIME OF CREATION 3
                    if int(table_data_clean[i][0] == 388):
                        table_data_trimmed.append(table_data_clean[i])
                        #AUTHORS
                    if int(table_data_clean[i][0]) == 700:
                        table_data_trimmed.append(table_data_clean[i])
                # extract strings
                extracted_data = [[isbn, 'isbn']]

                def extract_Title(string):
                    string = string.split('$c')[0]
                    string = string.split('$a')[1]
                    string = string.split('$b')[0] + string.split('$b')[1]
                    return string
                extracted_data.append([extract_Title(table_data_trimmed[1][2]), 'title'])


                def extract_Authors(data):
                    authors = []
                    authors_string = ''
                    for i in range(len(data)):
                        if int(data[i][0]) == 700:
                            string = data[i][2]
                            string = string.split('$a')[1]
                            string = string.split('$')[0]
                            string = string.strip()
                            string = string.replace(',', '')
                            authors.append(string)
                    for k in range(len(authors)):
                        if k == len(authors)-1:
                            authors_string = authors_string + authors[k]
                        else:
                            authors_string = authors_string + authors[k] + ', '
                    return authors_string
                extracted_data.append([extract_Authors(table_data_trimmed), 'authors'])


                def extract_Publisher(string):
                    string = string.split('$b')[1]
                    string = string.split('$c')[0]
                    string = string.replace(',', '')
                    string = string.strip()
                    return string
                extracted_data.append([extract_Publisher(table_data_trimmed[2][2]), 'Publisher'])

                for i in range(len(table_data_trimmed)):
                    print(table_data_trimmed[i])
                return extracted_data
        print(get_data(request.POST['ISBN'], 'BN'))
        return render(request, "isbn_search.html", context)
    else:
        return render(request, "no_permissions.html", {})

def success_view(request, *args, **kwargs):
    return render(request, "success.html", {})

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


def book_view(request, number, *args, **kwargs):
    obj = book.objects.get(id=number)
    context = {
        "object": obj,  
    }
    # context = {
    #     "title": "Czerwone Drzewo I magiczne krzesło",
    #     "author": "Andrzej Maleszka",
    #     "publisher": "Czarna Owca Wydawnictwo",
    #     "isbn": "0922114556655426",
    #     "description": "Chcesz zaprzyjaźnić się z Kukim, Tosią i Filipem? Wyrusz wraz z nimi do świata magii, który nie jest zarezerwowany tylko dla dzieci. Książka „Czerwone krzesło. Magiczne drzewo” Tom 1 pozwoli Ci poznać młode osoby, które mierzą się w życiu z wieloma trudnościami. W ich pokonaniu może pomóc tytułowe krzesło, które okazuje się magiczne.",
    #     "insert_date": "06.03.2022",
    #     "borrowed": False
    # }
    return render(request, 'book_view.html', context)
