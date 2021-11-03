#from typing import runtime_checkable
from django.db import models

# Create your models here.

class Proveedores(models.Model):
    nombres=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=50)
    razonsocial=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    ruc=models.CharField(max_length=11)
    celular=models.CharField(max_length=9)
    web=models.CharField(max_length=50)
    
    class Meta:
        verbose_name='Proveedor'
        verbose_name_plural='Proveedores'
        
    def __str__(self):
        return self.nombres 
  
