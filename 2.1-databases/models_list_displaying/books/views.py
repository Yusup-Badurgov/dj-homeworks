from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from books.models import Book


def index(request):
    return redirect('books')


def books_view(request):
    books = Book.objects.filter().order_by('pub_date')

    template = 'books/books_list.html'
    context = {
        'books': books
    }
    return render(request, template, context)


def detail_book_view(request, pub_date):
    books = Book.objects.filter().order_by('pub_date')
    book = books.get(pub_date=pub_date)
    print(book)
    pre_page = books.filter(pub_date__lt=pub_date).last()
    next_page = books.filter(pub_date__gt=pub_date).first()
    print(pre_page)
    print(next_page)

    template = 'books/detail.html'
    context = {
        'book': book,
        'pre_page': pre_page,
        'next_page': next_page,

    }

    return render(request, template, context=context)
