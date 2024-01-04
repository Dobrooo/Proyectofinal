from django.urls import path
from . import views
from .views import listaproductos,agregarempleado,agregarproveedor,agregarventa,eliminardetalleventa,eliminarventas,editardetalleventa,agregardetalle, listaventas, detalleproductos, editarproducto, agregarproducto, inicio, infousuarios, eliminarproducto, eliminarempleado, eliminarproveedor, infoproveedores, editarproveedor, detalleventas
from django.contrib.auth.views import LogoutView






urlpatterns = [
    #############################BASES############################

    path('', views.vista_base, name='base'),
    path('inventario', listaproductos.as_view(), name='inventario'),
    path('inicio', inicio.as_view(), name='inicio'),
    path('logout', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('empleados', infousuarios.as_view(), name='empleados'),
    path("proveedores", infoproveedores.as_view(), name="proveedores"),
    path('ventas', listaventas.as_view(), name='ventas'),

    #############################ELIMINAR############################

    path('eliminarproducto  /<int:pk>', eliminarproducto.as_view(), name='eliminarproducto'),
    path('eliminarempleado/<int:pk>', eliminarempleado.as_view(), name='eliminarempleado'),
    path('eliminarproveedor/<int:pk>', eliminarproveedor.as_view(), name='eliminarproveedor'),
    path('eliminarventa/<int:pk>', eliminarventas.as_view(), name='eliminarventa'),
    path('eliminardetalleventa/<int:pk>', eliminardetalleventa.as_view(), name='eliminardetalleventa'),
    #############################AÑADIR############################

    path('inventario/añadir', agregarproducto.as_view(), name='añadirproducto'),
    path('detalleventa/añadir', agregardetalle.as_view(), name='agregardetalleventa'),
    path('venta/añadir', agregarventa.as_view(), name='agregarventa'),
    path('empleados/añadir', agregarempleado.as_view(), name='agregarempleado'),
    path('proveedores/añadir', agregarproveedor.as_view(), name='agregarproveedor'),

    #############################DETALLES############################

    path('inventario/<int:pk>', detalleproductos.as_view(), name='detalle'),
    path('detalleventa', detalleventas.as_view(), name='detalleventa'),

    #############################EDITAR############################

    path('proveedores/<int:pk>', editarproveedor.as_view(), name='editarproveedor'),
    path('detalleventa/<int:pk>', editardetalleventa.as_view(), name='editardetalleventa'),
    path('inventario/editar/<int:pk>', editarproducto.as_view(), name='editar'),

    
    ]