# 'admin' permite acceder al panel de administración integrado de Django
from django.contrib import admin
# 'path' sirve para definir rutas y 'include' para conectar otros archivos urls.py
from django.urls import path, include

urlpatterns = [
    # ruta para el panel de administración de Django
    path('admin/', admin.site.urls),
    # redirige cualquier ruta vacía ('') a las URLs de la aplicación parcial1_app, toma prioridad la vista de home
    path('', include('parcial1_app.urls')),
]