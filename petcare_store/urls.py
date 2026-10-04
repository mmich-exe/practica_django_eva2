from django.contrib import admin
from django.urls import path
from inventario import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('categoria/<int:categoria_id>/', views.categoria_detalle, name='categoria'),
]

