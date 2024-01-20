from django.shortcuts import render
from .cart import Cart
from Apps.Home.models import Product
from django.shortcuts import redirect

# Create your views here.

# View 1
def add(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.add_product(product)
    return redirect('home')

# View 2
def delete(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.delete_product(product)
    return redirect('carro')

# View 3
def substract(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.substract_product(product)
    return redirect('carro')

# View 4
def clear(request, product_id):
    cart = Cart(request)
    cart.clear_cart()
    return redirect('carro')

def carro(request):
    return render(request, 'carro.html')