from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "category",
            "cost_price",
            "selling_price",
            "quantity",
        ]
