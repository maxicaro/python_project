from django import forms

class formulario_proveedor(forms.Form): 

 nombre = forms.CharField(max_length=30)
 apellido = forms.CharField(max_length=30)
 direccion = forms.CharField(max_length=50)
 email = forms.EmailField()
 telefono = forms.CharField(max_length=30)