from django.urls import path
from pedidos import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('',views.procesar_pedido, name='procesar_pedido'),
    
]