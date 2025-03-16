from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    # Поля, которые будут отображаться в списке пользователей
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    
    # Поля, по которым можно фильтровать пользователей
    list_filter = ('role', 'is_staff', 'is_superuser')
    
    # Поля, которые можно редактировать прямо из списка
    list_editable = ('role',)
    
    # Поля, по которым можно искать
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Группировка полей при редактировании пользователя
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'role')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    
    # Поля, которые отображаются при создании пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )