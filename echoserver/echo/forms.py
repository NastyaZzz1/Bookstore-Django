from django import forms
from .models import Books, Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class ItemForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'author', 'cost', 'genre']

labels = {
    'name': 'Название',
    'author': 'Автор',
    'cost': 'Стоимость',
    'genre': 'Жанр'
}

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'inp-login', 'placeholder': 'Ваше имя'}))
    last_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'inp-login', 'placeholder': 'Ваше имя'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'inp-login', 'placeholder': '@ username'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'inp-email', 'placeholder': 'Почта'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'inp-password', 'placeholder': 'Пароль',}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'inp-password-confirm', 'placeholder': 'Подтверждение пароля',}))

    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = Users
        fields = ['username', 'password']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email']