from django.urls import path
from .views import homePageView
from .views import addDataView
from . import views

urlpatterns = [
    path('', homePageView, name='home'),
    path('change_item/<int:item_id>/', views.changeDataView, name='change_item'),
    path('add_item/', addDataView, name='add_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('basket/', views.basket_view, name='basket'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/<int:item_id>/', views.delete_from_cart, name='delete_from_cart'),
    path('add_count_in_cart/<int:item_id>/', views.add_count_in_cart, name='add_count_in_cart'),
    path('orders/', views.orders_view, name='orders'),
    path('add_to_order/', views.add_to_order, name='add_to_order'),
]