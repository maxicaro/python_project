from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('login_usuario/',views.login_usuario, name='login_usuario'),
     path('login_admin/',views.login_admin, name='login_admin'),
     path('registro/',views.registro_usuario, name='registro'),
     path('logout/', views.logout_request, name='logout'),
     path('logout_admin/', views.logout_admin, name='logout_admin')
]
