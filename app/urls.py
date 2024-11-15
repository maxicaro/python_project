from app import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   
    
    path('cursos/', views.cursos,  name='cursos'),
    path('profesores/', views.profesores, name='profesores' ),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('pago_exitoso/', views.pago_exitoso, name='pago_exitoso'),
    path('index/', views.inicio, name='index' ),
    path('acerca_de/', views.acerca_de, name='acerca_de' ), 
    path('servicio/', views.servicio, name='servicio' ),
    path('cartera/', views.cartera, name='cartera' ),
    path('contacto/', views.contacto, name='contacto' ),
    path('contact/', views.contact, name='contacto_form'),
    path('contact_index/', views.contact_index, name='contact_index'),
    path('padre/', views.padre, name='padre' ),
    path('tienda/', views.tienda, name='tienda' ),
    path('productos/', views.productos, name='productos' ),
    path('productos_forms/', views.producto_forms, name='productos_forms' ),
    path('busqueda_producto/', views. busqueda_producto, name='busqueda_producto' ),
    path('buscar/', views.buscar, name='productos' ),
    path('clientes_forms/', views.clientes_forms, name='clientes_forms' ),
    path('proveedores_forms/', views.proveedores_forms, name='proveedores_forms' ),
    path('leer_proveedores/', views.leer_proveedores, name= 'leer_proveedores'),
    path('proveedores/', views.proveedores, name= 'proveedores'),
    path('eliminarproveedor/<proveedor_nombre>/',views.eliminarproveedor, name='eliminarproveedor'),
  # Incluye las URLs de la aplicación
  
  
    path('curso/list', views.CursoList.as_view(), name='List'),
    path('curso/<int:pk>/', views.CursoDetalle.as_view(), name='Detail'),
    path('nuevo/', views.CursoCreacion.as_view(), name='New'),
    path('curso/editar/<int:pk>/', views.CursoUpdate.as_view(), name='Edit'),
    path('curso/borrar/<int:pk>/', views.CursoDelete.as_view(), name='Delete'),
    
    path('cliente/list', views.ClienteList.as_view(), name='List_client'),
    path('cliente/<int:pk>/', views.ClienteDetalle.as_view(), name='List_Detail'),
    path('cliente_nuevo/', views.ClienteCreacion.as_view(), name='Client_New'),
    path('cliente/editar/<int:pk>/', views.ClienteUpdate.as_view(), name='List_Edit'),
    path('cliente/borrar/<int:pk>/', views.ClienteDelete.as_view(), name='List_Delete'),
    
    path('producto/list', views.ProductosList.as_view(), name='List_product'),
    path('producto/<int:pk>/', views.ProductosDetalle.as_view(), name='producto_Detail'),
    path('producto_nuevo/', views.ProductosCreacion.as_view(), name='producto_New'),
    path('producto/editar/<int:pk>/', views.ProductosUpdate.as_view(), name='producto_Edit'),
    path('producto/borrar/<int:pk>/', views.ProductosDelete.as_view(), name='producto_Delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   