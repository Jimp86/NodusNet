from django.contrib import admin

# Register your models here.
from Nodus.snippers import Attr
from Home.models import *

@admin.register(Principal)
class AdminPrincipal(admin.ModelAdmin):
    list_display_links = Attr(Principal)
    list_display = Attr(Principal)

@admin.register(DatosPrincipales)
class AdminDatosPrincipales(admin.ModelAdmin):
    list_display_links = Attr(DatosPrincipales)
    list_display = Attr(DatosPrincipales)

@admin.register(Nosotros)
class AdminHistoria(admin.ModelAdmin):
    list_display_links = Attr(Nosotros)
    list_display = Attr(Nosotros)

@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display_links = Attr(Slider)
    list_display = Attr(Slider)

@admin.register(Servicios)
class AdminServicios(admin.ModelAdmin):
    list_display_links = Attr(Servicios)
    list_display = Attr(Servicios)

@admin.register(Home)
class AdminHome(admin.ModelAdmin):
    list_display_links = Attr(Home)
    list_display = Attr(Home)

@admin.register(Pymes)
class AdminPymes(admin.ModelAdmin):
    list_display_links = Attr(Pymes)
    list_display = Attr(Pymes)

@admin.register(Planes)
class AdminPlanes(admin.ModelAdmin):
    list_display_links = Attr(Planes)
    list_display = Attr(Planes)


