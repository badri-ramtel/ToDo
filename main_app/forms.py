from typing import Any, Dict
from django import forms

# Create the form class.
class ToDoForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300, required=True, widget=forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'ENTER YOUR NAMEs'}))
