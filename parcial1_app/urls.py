from django.urls import path    # importa la función path para crear las direcciones URL de esta app
from . import views             # importa el archivo views.py de la misma carpeta (.) para usar sus funciones

urlpatterns = [
    # asocia la raíz ('') con la función 'home' en views.py
    path('', views.home, name='home'),
    # asocia la ruta 'about/' con la función 'about' en views.py
    path('about/', views.about, name='about'),
]