from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from users.forms import RegistroUsuarioForm
# Creamos la funcion login.



def login_usuario(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)
               # messages.success(request, f"Bienvenido {usuario}!")  # Mensaje de éxito
                return redirect("index")  # Redirige a la página principal o donde prefieras
            else:
                messages.error(request, "Error, datos incorrectos.")
                return redirect("login_usuario")
        else:
            messages.error(request, "Error en el formulario.")
    
    form = AuthenticationForm()
    return render(request, "user/login_usuario.html", {'form': form})
# Función de login para administradores
def login_admin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            # Verifica si el usuario es administrador (staff)
            if user is not None and user.is_staff:
                login(request, user)
                return render(request, "appt/padre.html", {"mensaje": f"Bienvenido, administrador {usuario}"})
            else:
                # Si el usuario no es administrador o los datos no son válidos
                messages.error(request, "Acceso denegado. Solo administradores pueden iniciar sesión.")
                return redirect('login_usuario')
        else:
            messages.error(request, "Error en el formulario.")
    
    form = AuthenticationForm()
    return render(request, "user/admin.html", {'form': form})

#Creamos la funcion register.


def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Autentica y registra al usuario automáticamente
            return redirect('index')  # Redirige a la página de inicio después del registro
    else:
        form = RegistroUsuarioForm()
    return render(request, 'user/registro.html', {'form': form})

# Nos deslogeamos.

#Deslogeo de usuarios.

def logout_request(request):
      logout(request)
     
      return render(request,"appt/index.html" )
  
  
#Deslogeo de administradores.

def logout_admin(request):
      logout(request)
     
      return render(request,"appt/padre.html" )