from django.db import models

#AHORA CREAMOS TABLAS

# Productos
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    codigo = models.IntegerField()
    seccion = models.ForeignKey('CategoriaProd', on_delete=models.CASCADE)  # Relación con CategoriaProd
    imagen = models.ImageField(upload_to="media", null=True, blank=True)
    precio = models.FloatField()
    proveedor = models.ForeignKey('Proveedores', on_delete=models.CASCADE)  # Relación con Proveedores
    created_at = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ="categoriaProd"
        verbose_name_plural ="categoriaProd"


    def __str__(self):
        return self.nombre

# Clientes
class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Proveedores
class Proveedores(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Pedidos
class Pedidos(models.Model):
    numero = models.IntegerField()
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)  # Relación con Clientes
    productos = models.ManyToManyField(Productos)  # Relación con Productos
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Pedido {self.numero} de {self.cliente}"
    
# Categoria
class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name ="categoriaProd"
        verbose_name_plural ="categoriaProd"

    def __str__(self):
        return self.nombre
