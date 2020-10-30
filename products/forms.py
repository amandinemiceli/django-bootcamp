from django import forms

from .models import Product

# class ProductForm(forms.Form):
#     title = forms.CharField()


class ProductModelForm(forms.ModelForm):
    # title = forms.CharField()
    class Meta:
        model = Product
        fields = [
            'title',
            'content'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 4:
            raise forms.ValidationError("The title is not long enough")
        return title

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 4:
            raise forms.ValidationError("The content is not long enough")
        return content