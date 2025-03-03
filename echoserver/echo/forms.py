from django import forms
from .models import Books


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