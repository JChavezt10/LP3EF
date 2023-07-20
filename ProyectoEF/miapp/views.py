from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def Paises(request):
    return render(request, 'Paises.html', )

def RegistrarPais(request):
    return render(request, 'RegistrarPais.html', )

def Editoriales(request):
    return render(request, 'Editoriales.html', )

def CrearEditorial(request):
    return render(request, 'CrearEditorial.html')