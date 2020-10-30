from django import forms

from .models import Product

# class ProductForm(forms.Form):
#     title = forms.CharField()


class ProductModelForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Product
        fields = [
            'title'
        ]