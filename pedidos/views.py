from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from carro.carro import Carro
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from pedidos.models import LineaPedido, PedidoCliente
from app.models import Productos
from django.urls import reverse

@login_required(login_url="/users/login_usuario")
def procesar_pedido(request):
    pedido = PedidoCliente.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido = []
    total_compra = 0  # Inicializamos el total de la compra

    for key, value in carro.carro.items():
        producto = Productos.objects.get(id=key)
        lineas_pedido.append(
            LineaPedido(
                producto_id=key,
                cantidad=value["cantidad"],
                user=request.user,
                pedido=pedido
            )
        )
        # Sumamos al total el precio de cada producto por su cantidad
        total_compra += producto.precio * value["cantidad"]

    LineaPedido.objects.bulk_create(lineas_pedido)

    # Extraer los datos para el correo
    productos_pedido = []
    for item in lineas_pedido:
        producto = Productos.objects.get(id=item.producto_id)
        productos_pedido.append({
            "nombre": producto.nombre,
            "precio": producto.precio,
            "cantidad": item.cantidad
        })

    enviar_mail(
        pedido=pedido,
        productos_pedido=productos_pedido,
        total_compra=total_compra,  # Pasamos el total de la compra al correo
        nombreusuario=request.user.username,
        emailusuario=request.user.email
    )

    messages.success(request, "El pedido se ha creado correctamente")
    return redirect(reverse('pago_exitoso'))

def enviar_mail(**kwargs):
    asunto = "Gracias por tu pedido"
    mensaje = render_to_string("appt/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "productos_pedido": kwargs.get("productos_pedido"),
        "total_compra": kwargs.get("total_compra"),  # Incluimos el total de la compra en el contexto
        "nombreusuario": kwargs.get("nombreusuario")
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "miguelphp1981@gmail.com"
    to = kwargs.get("emailusuario")

    send_mail(
        asunto,
        mensaje_texto,
        from_email,
        [to],
        html_message=mensaje
    )
