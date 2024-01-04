from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class usuarios(models.Model):
    idusuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    dni = models.PositiveIntegerField(blank=True, null=True)

class productos(models.Model):
    idproducto = models.AutoField(primary_key=True, blank=False, null=False)
    nombre = models.CharField(max_length=200, unique=True)
    precio_compra = models.FloatField(max_length=10)
    precio_venta = models.FloatField()
    stock = models.PositiveIntegerField(blank=True, null=True)
    stock_min = models.PositiveIntegerField(default=10)
    codbarras = models.PositiveIntegerField(unique=True)
   

class empleados(models.Model):
    dni = models.IntegerField(primary_key=True)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField( max_length=50)
    direccion = models.CharField( max_length=50)
    telefono = models.IntegerField()
    mail = models.EmailField(max_length=254)

class proveedores(models.Model):
    codproveedor = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

class ventas(models.Model):
    idventa = models.AutoField(primary_key=True)
    dni_empleado = models.ForeignKey(empleados, to_field='dni', on_delete=models.DO_NOTHING, null=True, blank=True)
    fecha = models.DateTimeField(auto_now=True, unique=True)
    importe = models.FloatField()

class detalle_venta(models.Model):
    idventadetalle = models.AutoField(primary_key=True)
    idventa = models.ForeignKey(ventas, to_field='idventa', on_delete=models.DO_NOTHING)
    producto = models.ForeignKey(productos, to_field='nombre', on_delete=models.DO_NOTHING)
    cantidad = models.PositiveIntegerField()
    importe_unit = models.FloatField()
