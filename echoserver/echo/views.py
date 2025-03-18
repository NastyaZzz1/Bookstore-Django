from django.shortcuts import get_object_or_404, redirect, render
from .models import *
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


def delete_item(item_id):
    item = get_object_or_404(Books, id=item_id)
    item.delete()
    return redirect('home')


def register(request):
    if request.method == 'POST':
        print("POST-данные:", request.POST)

        form = RegisterForm(request.POST)
        
        print("FORM:", form)

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
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_key = request.session.session_key
        cart = Cart.objects.filter(session_key=session_key).first()

    if not cart:
        cart = Cart.objects.create(user=request.user if request.user.is_authenticated else None,
                                  session_key=request.session.session_key if not request.user.is_authenticated else None)

    return render(request, 'html/basket.html', {'cart': cart})


def add_to_cart(request, item_id):
    product = get_object_or_404(Books, id=item_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.name} added to cart!")
    return redirect('home') 


def delete_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('basket')

def add_count_in_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.quantity += 1
    item.save()

    return redirect('basket')


def orders_view(request):
    
    
    return render(request, 'html/orders.html', {})
    