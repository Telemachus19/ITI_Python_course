from django import forms
from .models import Book, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'desc', 'rate', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter book description'}),
            'rate': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 5, 'placeholder': 'Rating (0-5)'}),
            'categories': forms.CheckboxSelectMultiple(),
        }

