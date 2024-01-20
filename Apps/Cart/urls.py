from django.urls import path
from . import views

app_name = 'Cart'
urlpatterns = [
    	path('', views.carro, name="carro"),
	path('add/<int:product_id>/',  views.add, name="add"),
	path('delete/<int:product_id>/',  views.delete, name="delete"),
	path('substract/<int:product_id>/',  views.substract, name="substract"),
	path('clear/',  views.clear, name="clear"),
	
]
