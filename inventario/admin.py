from django.contrib import admin
from .models import Categoria, Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'categoria', 'marca', 'precio', 'stock', 'disponible', 'destacado', 'requiere_refrigeracion')
    search_fields = ('codigo', 'nombre', 'marca')
    list_filter = ('categoria', 'disponible', 'destacado', 'requiere_refrigeracion')
    ordering = ('nombre',)
    