from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'price', 'phone', 'product_type', 'description',
                  'category', 'owner', 'image']