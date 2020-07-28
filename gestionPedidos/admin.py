from django.contrib import admin

# Register your models here.

from gestionPedidos.models import Clientes, Articulos, Pedidos #importo tablas desde models

class ClientesAdmin(admin.ModelAdmin): #con esta clase hago manipulaciones/modificaciones en la tabla de la base
    list_display=("nombre", "direccion", "telefono") #asi hago que se muestren los campos que quiero por tabla
    search_fields=("nombre", "telefono") #asi hago que se muestren casillas de busquedas 

class ArticulosAdmin(admin.ModelAdmin):
    list_filter=("seccion",) #lleva COMA ya que va a tirar tantas tuplas como productos haya

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    list_filter=("fecha",)
    date_hierarchy="fecha" #muestra recorrido de fecha tipo camino

#asi hago que se vean en el panel de administración 
admin.site.register(Clientes, ClientesAdmin) #incluyo la clase para oder mostrar los campos por tabla 
admin.site.register(Articulos, ArticulosAdmin)
admin.site.register(Pedidos, PedidosAdmin)