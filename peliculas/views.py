from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from peliculas.forms import PeliculaFormulario, KdmFormulario, SesionFormulario
from peliculas.models import Peliculas, Sesion, Kdm


# Create your views here.

def index(request): 
    bienvenida = "Bienvenido a la base de datos de peliculas"
    context = {
        "bienvenida": bienvenida
    }
    return render(request, "basepeliculas/inicio.html", context)


def listar_peliculas(request): 
    contexto = {
    "peliculas": Peliculas.objects.all() 
     }
    
    http_response = render(
    request=request,
    template_name= "basepeliculas/lista_peliculas.html",
    context = contexto , 
  ) 
    return http_response 
    
    
def listar_kdms(request):
    contexto = {
        "kdms": Kdm.objects.all()
    }
    http_response = render(
        request=request, 
        template_name= "basepeliculas/lista_kdms.html",
        context = contexto,
    ) 
    return http_response
    

def listar_sesiones(request): 
    contexto = {
    "sesiones": Sesion.objects.all() 
     }
    
    http_response = render(
    request=request,
    template_name= "basepeliculas/lista_sesiones.html",
    context = contexto , 
  ) 
    return http_response 


def buscar_pelicula(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda")  
        peliculas = Peliculas.objects.filter(titulo__contains=busqueda)
        contexto = {
            "peliculas": peliculas,  
        }
        return render(request, 'basepeliculas/lista_peliculas.html', context=contexto)
    else:  # Handle GET request
        return render(request, 'basepeliculas/lista_peliculas.html')
    
def buscar_kdm(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda")  
        kdm = Kdm.objects.filter(titulo_kdm__contains=busqueda)
        contexto = {
            "kdm": kdm,  
        }
        return render(request, 'basepeliculas/lista_kdms.html', context=contexto)
    else:  
        return render(request, 'basepeliculas/lista_kdms.html')
    
def buscar_sesion(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data.get("busqueda") 
        sala = Sesion.objects.filter(sala__contains=busqueda)
        contexto = {
            "sala": sala, 
        }
        return render(request, 'basepeliculas/lista_sesiones.html', context=contexto)
    else:  
        return render(request, 'basepeliculas/lista_sesiones.html')
        
    
def agregar_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            titulo = data["titulo"]
            version = data["version"]
            cpl = data["cpl"]
            pelicula = Peliculas(titulo=titulo, version=version, cpl=cpl)  
            pelicula.save()  

          
            url_exitosa = reverse('lista_peliculas')  
            return redirect(url_exitosa)
    else:  
        formulario = PeliculaFormulario()
    http_response = render(
        request=request,
        template_name="basepeliculas/formulario_pelicula.html",
        context={'formulario': formulario}
    )
    return http_response

def agregar_kdm(request):
    if request.method == "POST":
        formulario = KdmFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  
            titulo_kdm = data["titulo_kdm"]
            cpl_kdm = data["cpl_kdm"]
            servidor_kdm = data["servidor_kdm"]
            fecha_apertura = data["fecha_apertura"]
            fecha_clausura = data["fecha_clausura"]
            kdm = Kdm(titulo_kdm=titulo_kdm, cpl_kdm=cpl_kdm, servidor_kdm=servidor_kdm, fecha_apertura=fecha_apertura, fecha_clausura=fecha_clausura)  # lo crean solo en RAM
            kdm.save()  

           
            url_exitosa = reverse('lista_kdms') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = KdmFormulario()
    http_response = render(
        request=request,
        template_name="basepeliculas/formulario_kdm.html",
        context={'formulario': formulario}
    )
    return http_response

def agregar_sesion(request):
    if request.method == "POST":
        formulario = SesionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data 
            titulo_sesion = data["titulo_sesion"]
            version_sesion = data["version_sesion"]
            datetime_sesion = data["datetime_sesion"]
            sala = data["sala"]
            sesion = Sesion(titulo_sesion=titulo_sesion, version_sesion=version_sesion, datetime_sesion=datetime_sesion, sala=sala)  # lo crean solo en RAM
            sesion.save()  

            
            url_exitosa = reverse('lista_sesiones') 
            return redirect(url_exitosa)
    else:  # GET
     formulario = SesionFormulario()
     http_response = render(
        request=request,
        template_name="basepeliculas/formulario_sesion.html",
        context={'formulario': formulario}
    )
    return http_response