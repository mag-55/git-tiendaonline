from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedidos.forms import FormularioContacto

# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):
    if request.GET["prd"]:
        #mensaje="Artículo buscado: %r" %request.GET["prd"] #muestro mensaje en pagina
        producto=request.GET["prd"] #estos pasos son para buscar el articulo en la tabla Articulos
        if len(producto) > 20:
            mensaje="El texto de busqueda es demasiado largo"
        else:
            articulos=Articulos.objects.filter(nombre__icontains=producto)
            return render(request, "resultados_busquedas.html", {"articulos":articulos, "query":producto})
    else:
        mensaje="NO has introducido nada"
    return HttpResponse(mensaje)

def contacto(request):
    if request.method == "POST":

        miFormulario=FormularioContacto(request.POST) #instancio la clase con un parametro request para tomar datos
        if miFormulario.is_valid(): #veo si son validos
            inf_form=miFormulario.cleaned_data # cargo el diicionario en una variable
            send_mail(inf_form['asunto'], inf_form['mensaje'], inf_form.get('email', ''), ['anduezagerardo@gmail.com'],)
            return render(request, "gracias.html")

    else:
        miFormulario=FormularioContacto()
    
    return render(request, "formulario_contacto.html", {"form":miFormulario})



        #subject=request.POST["asunto"] #obtengo los datos para el email
        #message=request.POST["mensaje"] + " " + request.POST["email"]
        #email_from=settings.EMAIL_HOST_USER #quien lo envia
        #recipient_list=["anduezagerardo@gmail.com"] #a quien va o a que casilla de correo se envia
        #send_mail(subject, message, email_from, recipient_list)
        #return render(request, "gracias.html")

    #return render(request, "contacto.html")