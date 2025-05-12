
from django.urls import  path
from Aplicaciones.restaurant import views
from django.contrib.auth import views as auth_views

from .views import CustomLoginForm



urlpatterns = [
    path('', views.inicio, name='inicio' ),
    path('lista_menu/', views.lista_menu, name='lista_menu' ),
    path('crear_menu/', views.crear_menu, name='nuevo_menu' ),
    path('crear_bebida/', views.crear_bebidas, name='nueva_bebida' ),
    path('eliminar_menu/<int:idmen>', views.eliminar_menu, name="eliminar_menu"),
    path('eliminar_bebida/<int:id>', views.eliminar_bebida, name="eliminar_bebida"),
    path('lista_bebidas/', views.lista_bebidas, name="bebidas"),
    path('editar_menu/<int:id>', views.editar_menu, name="editar_menu"),
    
    path('tabla_menu/', views.tabla_menu, name="tabla_menu"),
    path('tabla_bebidas/', views.tabla_bebidas, name="tabla_bebidas"),
    
    path('contacto/', views.contacto, name="contacto"),
    path('latia/', views.latia, name="latia"),
    path('ubicacion/', views.ubicacion, name="ubicacion"),
    
    #autenticacion
    path('login/', auth_views.LoginView.as_view(template_name="auth/login.html", authentication_form=CustomLoginForm), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout' ),
    
    
    
    
]
