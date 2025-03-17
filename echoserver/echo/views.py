from django.shortcuts import get_object_or_404, redirect, render
from .models import Books
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import *



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


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'html/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'html/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')


def profile_view(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен!')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = ProfileEditForm(instance=request.user)

    return render(request, 'html/profile.html', {'form': form})


def basket_view(request):
     
     return render(request, 'html/basket.html', {})