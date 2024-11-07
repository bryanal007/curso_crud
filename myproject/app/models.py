from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre= models.CharField(max_length=100,blank=False, verbose_name="Nombre : " , help_text="introdusca solo valores de caracteres",editable=True)
    descripcion = models.TextField(max_length=2000, blank=True)
    precio = models.DecimalField(max_digits=4,decimal_places=2)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.nombre
