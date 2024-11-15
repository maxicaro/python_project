
#En nuestro archivo views.py de la app
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.models import Productos, Proveedores, Clientes

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView
from django.urls import reverse_lazy

#Decorador por defecto
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def inicio(req):
    return render(req, 'appt/index.html')

def pago_exitoso(req):
    return render(req, 'appt/pago_exitoso.html')

def padre(req):
    return render(req, 'appt/padre.html')

def productos(req):
    return render(req, 'appt/buscar_pro.html')

def tienda(req):
    productos = Productos.objects.all()
    return render(req, 'appt/tienda.html', {"productos": productos}) 

def acerca_de(req):
    return render(req, 'appt/acerca_de.html')

def servicio(req):
    return render(req, 'appt/servicio.html')

def cartera(req):
    return render(req, 'appt/cartera.html')

def contacto(req):
    return render(req, 'appt/contacto.html')

def proveedores(req):
    return render(req, 'appt/proveedores.html')

def cursos(req):
     return render(req, 'appt/cursos.html')

def profesores(req):
    return HttpResponse('vista profesores')

def estudiantes(req):
    return HttpResponse('vista estudiantes')

def entregables(req):
    return HttpResponse('vista entregables')

#======================================================================
# Envio de datos Productos.

def producto_forms(req):
    if req.method == 'POST':
        # Obtener los valores del formulario
        nombre = req.POST.get('nombre')
        codigo = req.POST.get('codigo')
        seccion = req.POST.get('seccion')
        precio = req.POST.get('precio')
        proveedor_nombre = req.POST.get('proveedor')

        # Verificar que todos los campos están presentes
        if nombre and codigo and seccion and precio and proveedor_nombre:
            # Buscar o crear el proveedor
            proveedor, created = Proveedores.objects.get_or_create(nombre=proveedor_nombre)

            # Crear y guardar el nuevo producto
            producto = Productos(nombre=nombre, codigo=codigo, seccion=seccion, precio=precio, proveedor=proveedor)
            producto.save()

            # Obtener la lista de todos los productos después de agregar el nuevo
            productos = Productos.objects.all().order_by('-created_at')

            # Redirigir o mostrar la lista de productos con un mensaje de éxito
            return render(req, "appt/leer_proveedores.html", {'mensaje': 'Producto agregado exitosamente', 'Productos': productos})


    # Si el método no es POST, mostrar el formulario
    return render(req, "appt/productos_forms.html")

#======================================================================
# Envio de datos Proveedores.
def proveedores_forms(req):
    if req.method == 'POST':
        # Obtener los valores del formulario
        nombre = req.POST.get('nombre')
        apellido = req.POST.get('apellido')
        direccion = req.POST.get('direccion')
        email = req.POST.get('email')
        telefono = req.POST.get('telefono')

        # Verificar que todos los campos están presentes
        if nombre and apellido and direccion and email and telefono:
            # Crear y guardar el nuevo proveedor
            proveedor = Proveedores(nombre=nombre, apellido=apellido, direccion=direccion, email=email, telefono=telefono)
            proveedor.save()

            # Obtener la lista de todos los proveedores después de agregar el nuevo
            proveedores = Proveedores.objects.all().order_by('-created_at')

            # Redirigir o mostrar la lista de proveedores con un mensaje de éxito
            return render(req, "appt/leer_proveedores.html", {'mensaje': 'Proveedor agregado exitosamente', 'Proveedores': proveedores})

    # Si el método no es POST, mostrar el formulario
    return render(req, "appt/proveedores_forms.html")

#======================================================================
# Envio de datos Clientes.

def clientes_forms(req):
    if req.method == 'POST':
        # Obtener los valores del formulario
        nombre = req.POST.get('nombre')
        apellido  = req.POST.get('apellido')
        direccion = req.POST.get('direccion')
        email = req.POST.get('email')
        telefono = req.POST.get('telefono')

        # Verificar que todos los campos están presentes
        if nombre and apellido  and direccion and email and telefono:
        

            # Crear y guardar el nuevo producto
            cliente = Clientes(nombre=nombre,  apellido=apellido , direccion=direccion, email=email, telefono=telefono)
            cliente.save()

             # Obtener la lista de todos los clientes después de agregar el nuevo
            clientes = Clientes.objects.all().order_by('-created_at')

            # Redirigir o mostrar la lista de clientes con un mensaje de éxito
            return render(req, "appt/leer_proveedores.html", {'mensaje': 'Cliente agregado exitosamente', 'Clientes': clientes})


    # Si el método no es POST, mostrar el formulario
    return render(req, "appt/clientes_forms.html")


#======================================================================
# Buesqueda de datos de productos.

def busqueda_producto(request):
     return render(request, 'appt/buscar_productos.html')
   
    
def buscar(request):
    if "codigo" in request.GET:
        codigo = request.GET["codigo"]
        productos = Productos.objects.filter(codigo__contains=codigo)
        return render(request, "appt/buscar_pro.html", {"nombre": productos, "codigo": codigo})
    else:
        return render(request, "appt/buscar_pro.html", {"nombre": [], "codigo": None})

#======================================================================
# Crud Proveedores.

def leer_proveedores(request):

      proveedores = Proveedores.objects.all() #trae todos los proveedores

      contexto= {"Proveedores":proveedores} 

      return render(request, "appt/leer_proveedores.html",contexto)
  
  #Eliminar.
  
def eliminarproveedor(request, proveedor_nombre):
    # Buscar el proveedor por nombre, si no existe, 'proveedor' será None
    proveedor = Proveedores.objects.filter(nombre=proveedor_nombre).first()

    # Verificar si el proveedor existe
    if proveedor:
        proveedor.delete()  # Eliminar el proveedor si existe
        mensaje = f"Proveedor '{proveedor_nombre}' eliminado correctamente."
    else:
        # Si no se encuentra el proveedor, mostrar un mensaje de error
        mensaje = f"El proveedor '{proveedor_nombre}' no existe o ya ha sido eliminado."

    # Obtener la lista actualizada de proveedores
    proveedores = Proveedores.objects.all()  # Trae todos los proveedores

    # Contexto para pasar a la plantilla
    contexto = {
        "Proveedores": proveedores,
        "mensaje": mensaje  # Añadimos el mensaje al contexto para mostrarlo en la plantilla
    }

    # Renderizar la plantilla con los proveedores actualizados y el mensaje
    return render(request, 'appt/leer_proveedores.html', contexto)
#Formulario.

#VISTAS DE CLASES PROVEEDORES:

class CursoList(LoginRequiredMixin,ListView):
    model = Proveedores
    template_name = "appt/proveedores_list.html"
    context_object_name = "object_list"
    
    # Ordenar por el campo de fecha de creación en orden descendente
    def get_queryset(self):
        return Proveedores.objects.all().order_by('-created_at')

class CursoDetalle(DetailView):
    model = Proveedores
    template_name = "appt/curso_detalle.html"

class CursoCreacion(CreateView):
    model = Proveedores
    template_name = 'appt/curso_form.html'
    success_url = reverse_lazy("List")
    fields = ['nombre', 'apellido', 'direccion', 'email', 'telefono']

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor agregado exitosamente.')
        return super().form_valid(form)

class CursoUpdate(UpdateView):
    model = Proveedores
    template_name = 'appt/curso_form.html'
    success_url = reverse_lazy("List")
    fields = ['nombre', 'apellido', 'direccion', 'email', 'telefono']

    def form_valid(self, form):
        messages.success(self.request, 'Proveedor actualizado correctamente.')
        return super().form_valid(form)

class CursoDelete(DeleteView):
    model = Proveedores
    success_url = reverse_lazy("List")
    template_name = 'appt/curso_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        # Obtener el proveedor que se está eliminando
        proveedor = self.get_object()

        # Llamar a la superclase para realizar la eliminación
        response = super().delete(request, *args, **kwargs)

        # Mostrar mensaje de éxito después de eliminar
        messages.success(self.request, f"Proveedor {proveedor.nombre} eliminado correctamente.")

        return response



#VISTAS DE CLASES CLIENTES:

class ClienteList(LoginRequiredMixin,ListView):
    model = Clientes
    template_name = "appt/cliente_list.html"
    context_object_name = "object_list"
    
    # Ordenar por el campo de fecha de creación en orden descendente
    def get_queryset(self):
        return Clientes.objects.all().order_by('-created_at')

class ClienteDetalle(DetailView):
    model = Clientes
    template_name = "appt/cliente_detalle.html"

class ClienteCreacion(CreateView):
    model = Clientes
    template_name = 'appt/clientes_forms.html'
    success_url = reverse_lazy("List_client")
    fields = ['nombre', 'apellido', 'direccion', 'email', 'telefono']

    def form_valid(self, form):
        messages.success(self.request, 'Cliente agregado exitosamente.')
        return super().form_valid(form)

class ClienteUpdate(UpdateView):
    model = Clientes
    template_name = 'appt/clientes_forms.html'
    success_url = reverse_lazy("List_client")
    fields = ['nombre', 'apellido', 'direccion', 'email', 'telefono']

    def form_valid(self, form):
        messages.success(self.request, 'Cliente actualizado correctamente.')
        return super().form_valid(form)

class ClienteDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy("List_client")
    template_name = 'appt/cliente_delete.html'

    def delete(self, request, *args, **kwargs):
        # Obtener el proveedor que se está eliminando
        proveedor = self.get_object()

        # Llamar a la superclase para realizar la eliminación
        response = super().delete(request, *args, **kwargs)

        # Mostrar mensaje de éxito después de eliminar
        messages.success(self.request, f"Cliente {proveedor.nombre} eliminado correctamente.")

        return response


#VISTAS DE CLASES PRODUCTOS:

class ProductosList(LoginRequiredMixin,ListView):
    model = Productos
    template_name = "appt/producto_list.html"
    context_object_name = "object_list"
    
    # Ordenar por el campo de fecha de creación en orden descendente
    def get_queryset(self):
        return Productos.objects.all().order_by('-created_at')

class ProductosDetalle(DetailView):
    model = Productos
    template_name = "appt/producto_detalle.html"

class ProductosCreacion(CreateView):
    model = Productos
    template_name = 'appt/forms_producto.html'
    success_url = reverse_lazy("List_product")
    fields = ['nombre', 'codigo', 'seccion', 'precio','proveedor','imagen']

    def form_valid(self, form):
        messages.success(self.request, 'Producto agregado exitosamente.')
        return super().form_valid(form)

class ProductosUpdate(UpdateView):
    model = Productos
    template_name = 'appt/editar_producto.html'
    success_url = reverse_lazy("List_product")
    fields = ['nombre', 'codigo', 'seccion', 'precio','proveedor','imagen']

    def form_valid(self, form):
        messages.success(self.request, 'Producto actualizado correctamente.')
        return super().form_valid(form)

class ProductosDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy("List_product")
    template_name = 'appt/producto_delete.html'

    def delete(self, request, *args, **kwargs):
        # Obtener el proveedor que se está eliminando
        proveedor = self.get_object()

        # Llamar a la superclase para realizar la eliminación
        response = super().delete(request, *args, **kwargs)

        # Mostrar mensaje de éxito después de eliminar
        messages.success(self.request, f"Producto {proveedor.nombre} eliminado correctamente.")

        return response


#======================================================================
# Envio de correos contacto.html.

def contact(request):
    if request.method == 'POST':
        name = request.POST['nombre_completo']
        telefono = request.POST['telefono']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('appt/email.html', {
            'name': name,
            'telefono': telefono,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['miguelphp1981@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')
        return redirect('contacto')


#======================================================================
# Envio de correos index.hml.

def contact_index(request):
    if request.method == 'POST':
        name = request.POST['nombre_completo']
        telefono = request.POST['telefono']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('appt/email.html', {
            'name': name,
            'telefono': telefono,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['miguelphp1981@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        messages.success(request, 'El correo electrónico se envió correctamente')
        return redirect('index')

  