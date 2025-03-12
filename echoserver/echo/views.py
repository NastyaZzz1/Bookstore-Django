from django.shortcuts import get_object_or_404, redirect, render
from .forms import ItemForm
from .models import Books
from django.core.paginator import Paginator



def homePageView(request):
    all_books = Books.objects.all()
    count = Books.objects.all().count()

    paginator = Paginator(all_books, 9)

    page_number = request.GET.get('page')

    page_obj = paginator.get_page(page_number)

    context = {
        'all_books' : all_books,
        'count' : count,
        'page_obj' : page_obj   
    }
    return render(request, 'html/book_catalog.html', context=context)



def changeDataView(request, item_id):
    book = get_object_or_404(Books, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=book)

    return render(request, 'html/change_book.html', {'form': form, 'book': book})



def addDataView(request):
    if request.method == "POST":
        book = Books()
        book.name = request.POST.get("name")
        book.author = request.POST.get("author")
        book.cost = request.POST.get("cost")
        book.genre = request.POST.get("genre")
        book.save()
        return redirect('home')
    else :
        return render(request, 'html/add_book.html', context={})


def delete_item(request, item_id):
    item = get_object_or_404(Books, id=item_id)
    item.delete()
    return redirect('home')