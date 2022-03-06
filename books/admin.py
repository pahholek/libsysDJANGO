from django.contrib import admin
from .models import book, user
# Register your models here.

admin.site.register(book)
admin.site.register(user)