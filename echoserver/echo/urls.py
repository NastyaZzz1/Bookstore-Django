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
]