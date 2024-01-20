def total_price(request):
    cart = request.session.get('cart', {})  # Use get with a default value to avoid KeyError

    total_price = 0

    if isinstance(cart, dict):
        for key, value in cart.items():
            # Calculate the total price based on the cart items
            total_price += value['price'] * value['quantity']

    return {'total_price': total_price}