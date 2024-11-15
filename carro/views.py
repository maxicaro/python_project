from django.shortcuts import render
from .carro import Carro
from app.models import Productos
from django.shortcuts import redirect

# Creacion de las views Carro.


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)  # Cambiado a Productos.objects.get
    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)  # Cambiado a Productos.objects.get
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Productos.objects.get(id=producto_id)  # Cambiado a Productos.objects.get
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")