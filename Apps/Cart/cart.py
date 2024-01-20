class Cart:
	def __init__(self, request):
		self.request = request
		self.session = request.session
		cart = self.session.get('cart')
		
		if not cart:
			cart = self.session["cart"] = {}
		else:
			self.cart = cart
	
	def add_product(self, product):
		product_id = str(product.id)
		product_data = self.cart.get(product_id, {})
		
		if not product_data:
			product_data = {
				"product_id": product_id,
				"name": product.name,
				"price": str(product.price),
				"quantity": 1,
				"image": product.image.url,
			}
		else:
			product_data["quantity"] += 1
		
		self.cart[product_id] = product_data
		self.save_cart()
	
	def save_cart(self):
		self.session["cart"] = self.cart
		self.session.modified = True
	
	def delete_product(self, product):
		product_id = str(product.id)
		if product_id in self.cart:
			del self.cart[product_id]
			self.save_cart()
	
	def substract_product(self, product):
		product_id = str(product.id)
		product_data = self.cart.get(product_id)
		
		if product_data:
			product_data["quantity"] -= 1
			if product_data["quantity"] == 0:
				self.delete_product(product)
	
	def clear_cart(self):
		self.session["cart"] = {}
		self.session.modified = True