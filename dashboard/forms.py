from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = 'Nome'
        self.fields['category'].label = 'Categoria'
        self.fields['quantity'].label = 'Quantidade'

    class Meta:
        model = Product
        fields = ['name', 'category', 'quantity']

class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].label = 'Produto'
        self.fields['order_quantity'].label = 'Quantidade'

    class Meta:
        model = Order
        fields = ['product', 'order_quantity']

