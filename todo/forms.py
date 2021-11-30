from django import forms 
from .models import *
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Post
        fields="__all__" 