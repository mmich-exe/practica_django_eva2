from django.shortcuts import render, get_object_or_404
from .models import Categoria, Producto

def inicio(request):
    categorias = Categoria.objects.all()
    destacados = Producto.objects.filter(destacado=True, disponible=True)

    return render(request, 'inventario/inicio.html', {
        'categorias': categorias,
        'destacados': destacados
    })

def categoria_detalle(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = Producto.objects.filter(categoria=categoria, disponible=True)

    return render(request, 'inventario/categoria.html', {
        'categoria': categoria,
        'productos': productos
    })