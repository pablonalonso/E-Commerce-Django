from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request, category=None):
	
    if category:
        # Filtra productos por la categoría seleccionada
        filtered_products = Product.objects.filter(categoria=category)
    else:
        # Si no se selecciona una categoría, obtener todos los productos
        filtered_products = Product.objects.all()

    return render(request, "home.html", {"products": filtered_products})

def wa_link_view(request, wa_link):
    return HttpResponse(f"Your custom response for wa.link: {wa_link}")

