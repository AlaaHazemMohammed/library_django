from django import forms
from .models import *


class catrgoryadd(forms.ModelForm):
    class Meta:
        model = category 
        fields = [
            'name'
        ]
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }


class addbook(forms.ModelForm):
    class Meta:
        model = Book 
        fields = [
            'title',
            'author' ,
            'photo_book' ,
            'photo_author' ,
            'pages' ,
            'price' ,
            'retal_price_day' ,
            'retal_period' ,
            'total_price' ,
            'active' ,
            'status' ,
            'category' 
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'photo_book':forms.FileInput(attrs={'class':'form-control'}),
            'photo_author':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day':forms.NumberInput(attrs={'class':'form-control','id':'retal_price_day'}),
            'retal_period':forms.NumberInput(attrs={'class':'form-control','id':'retal_period'}),
            'total_price':forms.NumberInput(attrs={'class':'form-control','id':'total_price'}),
            'active':forms.TextInput(attrs={'class':'form-control'}),
            'status':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'})
        }