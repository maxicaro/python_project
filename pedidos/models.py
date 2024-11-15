from django.db import models
from django.contrib.auth import get_user_model
from app.models import Productos
from django.db.models import F, Sum, FloatField
# Create your models here.

User=get_user_model()

class PedidoCliente(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) # Relación con LineaPedidos de los ID de usuarios
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return self.id
    
    @property
    def total(self):
     return self.lineapedido_set.aggregate(
         
         total=Sum(F("precio")*F("cantidad"), output_field=FloatField())
     )["total"]
    
    
    class Meta:
      db_table='pedidos'
      verbose_name='pedido'
      verbose_name_plural='pedidos'
      ordering=['id']
      
      
class LineaPedido(models.Model):
     user=models.ForeignKey(User, on_delete=models.CASCADE) # Relación con PedidoCliente de los ID de usuarios
     producto=models.ForeignKey(Productos, on_delete=models.CASCADE)  # Relación con Productos
     pedido=models.ForeignKey(PedidoCliente, on_delete=models.CASCADE) # Relación con PedidoCliente
     cantidad = models.IntegerField(default=1)
     created_at=models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
         return f'{self.cantidad} unidades de {self.producto.nombre}'
     
     class Meta:
      db_table='lineapedidos'
      verbose_name='Linea Pedido'
      verbose_name_plural='Lineas Pedidos'
      ordering=['id']
    
