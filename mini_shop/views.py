from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests




@login_required
def order_minishop(request):
    response = requests.get('http://localhost:8000/api/customers').json()
    return render(request, 'mini_shop/order.html')






