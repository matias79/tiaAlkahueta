from .models import Menu, Producto
from django.shortcuts import redirect, render
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def lista_menu(request):
    menu = Menu.objects.all()
    context= {
        'menus':menu
    }
    return render(request, 'restaurant/menu.html', context)


def lista_bebidas(request):
    bebida = Producto.objects.all()
    context = {
        'productos': bebida
    }
    return render(request, 'restaurant/bebidas.html', context)

@login_required(login_url='/login/')
def crear_menu(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        descripcion = request.POST['detalle']
        imagen = request.POST['imagen']
        Menu.objects.create(platoMenu = nombre, precioMenu = precio, descripcionMenu = descripcion, imagenMenu = imagen)
        return redirect('/lista_menu')
    else:
        return render(request, 'restaurant/crear_menu.html')

def editar_menu(request, id):
    menu = Menu.objects.filter(idMenu=id)
    return render(request, 'restaurant/editar_menu', {'menu':menu})
    """if request.method == 'POST':
        if request.POST.get("nombre") and request.POST.get("precio") and request.POST.get("detalle") and request.POST.get("imagen"):
            menu = Menu.objects.get(idMenu=id)
            menu.platoMenu=request.POST.get("nombre")
            menu.precioMenu=request.POST.get("precio")
            menu.descripcionMenu=request.POST.get("detalle")
            menu.imagenMenu=request.POST.get("imagen")
            menu.save()
            return render(request, 'restaurant/tablamenu.html')
        else:
            menu = Menu.objects.filter(idMenu=id)
            context = {
                'menu': menu
                }
            return render(request, 'restaurant/tablamenu.html', context)"""
        
      

@login_required(login_url='/login/')
def eliminar_menu(request, idmen):
    menu = Menu.objects.get(idMenu=idmen)
    menu.delete()
    return redirect('lista_menu')

@login_required(login_url='/login/')
def eliminar_bebida(request, id):
    bebida = Producto.objects.get(idProd=id)
    bebida.delete()
    return redirect('/lista_bebidas')


@login_required(login_url='/login/')
def crear_bebidas(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        fecha = request.POST['fecha']
        descripcion = request.POST['detalle']
        imagen = request.POST['imagen']
        Producto.objects.create(nombreProd = nombre, precioProd = precio, fecha_creacion_prod = fecha, descripcionProd=descripcion, imagenProd = imagen)
        return redirect('/lista_bebidas')
    else:
        return render(request, 'restaurant/crear_bebida.html')
    
def editar_bebida(request, id):
    bebida = Producto.objects.get(idProd=id)
    return render(request, 'restaurant/editar_bebida.html', {'bebida': bebida})
    
        
            


@login_required(login_url='/login/')
def tabla_menu(request):
    menu = Menu.objects.all()
    context= {
        'menus':menu
    }
    return render(request, 'restaurant/tablamenu.html', context)

@login_required(login_url='/login/')
def tabla_bebidas(request):
    bebida = Producto.objects.all()
    context= {
        'bebidas':bebida
    }
    return render(request, 'restaurant/tablabebidas.html', context)




#views de datos como contacto, ubicacion quines somos
def contacto(request):
    return render(request, 'datos/contact.html')

def latia(request):
    return render(request, 'datos/latia.html')

def ubicacion(request):
    return render(request, 'datos/ubicacion.html')






#login
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':'Usuario'},
    ), label='Usuario')
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña'}),
        label='Contraseña',
    )