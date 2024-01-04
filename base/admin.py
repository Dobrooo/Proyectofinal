from django.contrib import admin
from .models import User,usuarios,empleados,proveedores,productos,ventas,detalle_venta
# Register your models here.
admin.site.register(usuarios)
admin.site.register(empleados)
admin.site.register(proveedores)
admin.site.register(productos)
admin.site.register(ventas)
admin.site.register(detalle_venta)