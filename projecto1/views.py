from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader
from app.models import Productos

def saludo(request):
    return HttpResponse("Hola Django")

def otra_vista(request):
    return HttpResponse("<h1>¡Esto es un título!</h1><p>Y este es un párrafo.</p>")

def dia_de_hoy(request):
    hoy = date.today()
    return HttpResponse(f"Hoy es {hoy}")

def muestra_nombre(self, nombre):
    return HttpResponse(f"Buenos días {nombre}, bienvenido!!!")

# Agregamos al encabezado del archivo el import de Template y de Context


def probando_template(request):
    
    nom = "Juan"
    ap = "Perez"
    lista_notas = [1,2,3,4,5,6,7,8,9,10]
    diccionario_de_contexto = {'nombre': nom, 'apellido': ap, "hoy": datetime.now(), "notas": lista_notas}

    plantilla = loader.get_template('template1.html')
    
    documento = plantilla.render(diccionario_de_contexto)
    
    return HttpResponse(documento)


def agregar_producto(request, nom, cod):
    
 producto = Productos(nombre= nom, codigo= cod)

 producto.save()

 return HttpResponse("Producto agregado")