from django.contrib import admin
from .models import PedidoCliente, LineaPedido

# Registrar el modelo pedidos.
admin.site.register([PedidoCliente, LineaPedido])


