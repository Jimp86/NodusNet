from django.shortcuts import render

# Create your views here.


from Home.models import Principal, Slider, Nosotros, Servicios, DatosPrincipales, Home, Pymes


def index(request):
    contexto={
        "datosPrincipales": DatosPrincipales.objects.last(),
        "principal": Principal.objects.last(),
        "sliders": Slider.objects.all(),
        "nosotros": Nosotros.objects.all(),
        "servicios": Servicios.objects.all(),
        "home": Home.objects.all(),
        "pymes": Pymes.objects.all(),

        # "historia":Nosotros.objects.filter(tipo="Historia").first(),
        # "pasion":Nosotros.objects.filter(tipo="Pasion").first(),
        # "equipos":Equipo.objects.all(),
    }
    return render(request,"index.html",contexto)

#def historia(request):
#    historias=Nosotros.objects.filter(tipo="Historia")
#    for historia in historias:
#        historia.visitas+=1
#        historia.save()

#    contexto={
#        "principal": Principal.objects.last(),
#        "historias":historias,
#        "datosPrincipales": DatosPrincipales.objects.last(),
#    }
#    return render(request,"historia.html",contexto)

#def pasion(request):
#    historias=Nosotros.objects.filter(tipo="Pasion")
#    for historia in historias:
#        historia.visitas+=1
#        historia.save()

#    contexto={
#        "principal": Principal.objects.last(),
#        "historias":historias,
#        "datosPrincipales": DatosPrincipales.objects.last(),
#    }
#    return render(request,"pasion.html",contexto)

#def proyectos(request):
#    proyectos=Proyectos.objects.all()
#    categoria=None
#    if request.GET.get("projects"):
#        proyectos=Proyectos.objects.filter(categoria=request.GET.get("projects"))
#        categoria=Categoria.objects.get(id=request.GET.get("projects"))
#    contexto = {
#        "categorias":Categoria.objects.all(),
#        "proyectos":proyectos.order_by("nombre"),
#        "categoria":categoria,
#        "principal":Principal.objects.last(),
#        "datosPrincipales": DatosPrincipales.objects.last(),
#    }

#    return render(request,"proyectos.html",contexto)

#def blogs(request):
#    contexto={
#        'blogs':Blog.objects.all().order_by('-id'),
#        "datosPrincipales": DatosPrincipales.objects.last(),
#    }
#    return render(request,'blog2.html',contexto)

#def blog(request,id):
#    blog=Blog.objects.get(id=id)
#    blog.visitas+=1
#    blog.save()
#    contexto={
#        "blog":blog,
#        "datosPrincipales": DatosPrincipales.objects.last(),
#    }
#    return render(request, 'blog.html', contexto)

