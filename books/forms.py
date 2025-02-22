from django import forms
from .models import book

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['title','author','published_data', 'isbn', 'description']