from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 

# Create your views here.
def volver_atras(resquest,url_destino):
    return HttpResponseRedirect(reverse(url_destino))

def index(request):
    return render(request, 'templateApp/index.html')

def renderTemplate(request):
    data ={"ID":"2127798-5",
           "nombre":"Aaron segura",
           "email":"aaronsegura@gmail.com"}

    return render(request, 'templateApp/primeraweb.html',data)

def alimentos (request):
    data = {"nombre":"Aliemnto",
            "foto1":"arroz.png",
            "foto2":"pizza.png",
            "foto3":"ramen.png",
            "Aalimento1":"Arroz",
            "Alimento2":"Pizza",
            "Alimento3":"Ramen"}
    
    return render(request, 'templateApp/alimento.html',data)

def bebidas (request):
    data = {"nombre":"Bebida",
            "foto1":"soda.png",
            "foto2":"cerveza.png",
            "foto3":"cafe.png",
            "Bebidas":"COLA",
            "Bebidas":"Cerveza",
            "Bebidas":"Cafe"}
    
    return render(request, 'templateApp/bebidas.html',data)

def postres (request):
    data = {"nombre":"postre",
            "foto1":"pastel.png",
            "foto2":"helado", 
            "foto3":"galletas",
            "Postres":"Pastel",
            "Postres":"Helado",
            "Postres":"Galletas"}
    
    return render(request, 'templateApp/postres.html',data)

def alimento1 (request):
    return render (request,'templateAPP/alimento1.html')

def alimento2 (request):
    return render (request,'templateAPP/alimento2.html')

def alimento3 (request):
    return render (request,'templateAPP/alimento3.html')
    
def bebida1 (request):
    return render (request,'templateAPP/bebida1.html')
    
def bebida2 (request):
    return render (request,'templateAPP/bebida2.html')
    
def bebida3 (request):
    return render (request,'templateAPP/bebida3.html')

def postre1 (request): 
    return render (request,'templateAPP/postre1.html')

def postre2 (request): 
    return render (request,'templateAPP/postre2.html')

def postre3 (request): 
    return render (request,'templateAPP/postre3.html')

