from django.shortcuts import render
from django.http import HttpResponse
from .models import Books


def homePageView(request):
    all_books = Books.objects.all()
    count = Books.objects.all().count()

    context = {
        'all_books' : all_books,
        'count' : count    
    }

    return render(request, 'html/book_catalog.html', context=context)