from django.shortcuts import render

# definición para procesar la página de inicio
def home(request):
    return render(request, "parcial1/home.html")

# definición para procesar la página de información
def about(request):
    return render(request, "parcial1/about.html") # busca el archivo about.html dentro de la carpeta de templates