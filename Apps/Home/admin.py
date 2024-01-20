from django.contrib import admin
from .models import Product
from .models import Categoria

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'actualizado')


admin.site.register(Product, ProductAdmin)
admin.site.register(Categoria)
