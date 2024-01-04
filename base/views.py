from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import UpdateView, CreateView, DetailView, ListView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import productos,proveedores,empleados,detalle_venta,ventas,usuarios
# Create your views here.

def vista_base(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

class inicio(LoginView):
    model = usuarios
    template_name = 'inicio.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('empleados')


#############################LISTAS############################3


class infousuarios(LoginRequiredMixin, ListView):
    model= empleados
    template_name = 'empleados.html'
    
class infoproveedores(LoginRequiredMixin, ListView):
    model = proveedores
    template_name = 'proveedores.html'
    login_required = True


class listaventas(LoginRequiredMixin, ListView):
    model = ventas
    template_name = 'ventas.html'

class detalleventas(LoginRequiredMixin, ListView):
    model = detalle_venta
    template_name = 'detalleventa.html'
    template = loader.get_template('detalleventa.html')
    login_required = True

class listaproductos(LoginRequiredMixin, ListView):
    model = productos
    template_name = 'inventario.html'
    template = loader.get_template('inventario.html')
    login_required = True


#############################EDICIONES############################

class editardetalleventa(LoginRequiredMixin, UpdateView):
    model = detalle_venta
    fields = '__all__'
    template_name = 'editar.html'
    template = loader.get_template('editar.html')
    login_required = True
    success_url = reverse_lazy('detalleventa')


class editarproveedor(LoginRequiredMixin, UpdateView):
    model = proveedores
    fields = '__all__'
    template_name = 'editar.html'
    template = loader.get_template('editar.html')
    login_required = True
    success_url = reverse_lazy('proveedores')


class editarproducto(LoginRequiredMixin, UpdateView):
    model = productos
    context_object_name = 'editarpr'
    fields = '__all__'
    template_name = 'editar.html'
    template = loader.get_template('editar.html')
    success_url = reverse_lazy('inventario')
    login_required = True



#############################ELIMINAR############################

class eliminarempleado(LoginRequiredMixin, DeleteView):
    model = empleados
    template_name = 'eliminar.html'
    success_url = reverse_lazy('inicio')

class eliminarproducto(LoginRequiredMixin, DeleteView):
    model = productos
    template_name = 'eliminar.html'
    success_url = reverse_lazy('inicio')

class eliminarproveedor(LoginRequiredMixin, DeleteView):
    model = proveedores
    template_name = 'eliminar.html'
    success_url = reverse_lazy('inicio')

class eliminarventas(LoginRequiredMixin, DeleteView):
    model = ventas
    template_name = 'eliminar.html'
    success_url = reverse_lazy('ventas')

class eliminardetalleventa(LoginRequiredMixin, DeleteView):
    model = detalle_venta
    template_name = 'eliminar.html'
    success_url = reverse_lazy('detalleventa')



#############################DETALLES############################


class detalleproductos(LoginRequiredMixin, DetailView):
    model = productos
    context_object_name = 'detallepr'
    template_name = 'detalle.html'
    template = loader.get_template('detalle.html')
    login_required = True



#############################CREAR############################



class agregarproducto(LoginRequiredMixin, CreateView):
    model = productos
    fields = '__all__'
    template_name = 'añadirelemento.html'
    template = loader.get_template('añadirelemento.html')
    success_url = reverse_lazy('inventario')
    login_required = True


class agregardetalle(LoginRequiredMixin, CreateView):
    model = detalle_venta
    fields = '__all__'
    template_name = 'añadirelemento.html'
    template = loader.get_template('añadirelemento.html')
    success_url = reverse_lazy('ventas')
    login_required = True

class agregarventa(LoginRequiredMixin, CreateView):
    model = ventas
    fields = '__all__'
    template_name = 'añadirelemento.html'
    template = loader.get_template('añadirelemento.html')
    success_url = reverse_lazy('ventas')
    login_required = True

class agregarempleado(LoginRequiredMixin, CreateView):
    model = empleados
    fields = '__all__'
    template_name = 'añadirelemento.html'
    template = loader.get_template('añadirelemento.html')
    success_url = reverse_lazy('empleados')

class agregarproveedor(LoginRequiredMixin, CreateView):
    model = proveedores
    fields = '__all__'
    template_name = 'añadirelemento.html'
    template = loader.get_template('añadirelemento.html')
    success_url = reverse_lazy('proveedores')
