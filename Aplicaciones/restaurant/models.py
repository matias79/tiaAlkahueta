from django.db import models

# Create your models here.

    
class Producto(models.Model):
    idProd=models.AutoField(primary_key=True)
    nombreProd=models.CharField(max_length=150, null=False)
    precioProd=models.IntegerField()
    fecha_creacion_prod = models.DateField()
    descripcionProd=models.CharField(max_length=150)
    imagenProd=models.CharField(max_length=255)
    #logo_prod = models.FileField(upload_to='productos', null=True) #con esto se creara  la carpeta carreras en la carpeta media al cargar la imagen
    
    def __str__(self):
        return self.nombreProd
    
class Menu(models.Model):
    idMenu=models.AutoField(primary_key=True)
    platoMenu=models.CharField(max_length=50)
    precioMenu = models.IntegerField(null=True)
    descripcionMenu=models.CharField(max_length=150)
    imagenMenu=models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.platoMenu