from django.contrib import admin
from app.models import Productos, Clientes, Proveedores, Pedidos, CategoriaProd

# Registrar los modelos.

admin.site.register(Productos)
admin.site.register(Clientes)
admin.site.register(Proveedores)
admin.site.register(Pedidos)
admin.site.register(CategoriaProd)
