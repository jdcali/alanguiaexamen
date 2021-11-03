from django.contrib import admin
from .models import Proveedores

class ProveedoresAdmin (admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'razonsocial', 'direccion', 'ruc','celular','web')

admin.site.register(Proveedores, ProveedoresAdmin)
# Register your models here.
