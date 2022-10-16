from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404

from .models import CartProducts, Product

from products.models import Product

from carts.utils import get_or_create_cart

from .models import Cart

def cart(request):
    #request.session['cart_id'] = None

    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {
        'cart':cart
    })

def add(request):
    #importamos el carrito
    cart = get_or_create_cart(request)
    #Obtenemos el id del producto
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    quantity = int(request.POST.get('quantity', 1))

    #Como hay una relación de mnuchos a mnuchos
    #cart.products.add(product, through_defaults = {
    #    'quantity': quantity 
    #})

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart, product=product, quantity=quantity)

    return render(request, 'carts/add.html', {
        'quantity': quantity,
        'cart_product' : cart_product,
        'product': product
    })

def remove(request):
    cart = get_or_create_cart(request)
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))

    cart.products.remove(product)

    return redirect('carts:cart')