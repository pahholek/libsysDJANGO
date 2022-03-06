"""libsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from pages.views import *

urlpatterns = [
    #navbars urls
    path('', home_view, name='home'),
    path('dodajwolumin', add_book_view, name='dodajwolumin'),
    path('dodajczytelnika', add_reader_view, name='dodajczytelnika'),
    path('wypozycz', borrow_view, name='wypozycz'),
    path('zwrot', giveback_view, name='zwrot'),
    path('wyszukajczytelnik', search_reader_view, name='wyszukajc'),
    path('wyszukajksiazka', search_book_view, name='wyszukajk'),
    path('listaksiazka', book_list_view, name='listaksiazka'),
    path('listaczytelnik', reader_list_view, name='listaczytelnik'),
    path('podglangksiazka', book_view, name='podglangksiazka'), 
    path('admin/', admin.site.urls),    
]
