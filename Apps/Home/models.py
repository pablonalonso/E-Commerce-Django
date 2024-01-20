from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)
  

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        

    def __str__(self):
        return self.nombre

class Product(models.Model):
    titulo = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    mililitros = models.IntegerField(null=True)
    imagen = models.ImageField(upload_to='images', null=True, default='default_image.jpg', max_length=300)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.titulo

