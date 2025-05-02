from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import buscar_skin, BuscarSkin
from home.models import Skin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy


def inicio(request):
    #return HttpResponse("<h1>HOLA</h1>")
    return render(request, "home/inicio.html")

def buscar_skin(request):  # esta es tu vista con el mismo nombre
    if request.method == "POST":
        formulario = BuscarSkin(request.POST)  # ¡esto es el formulario!
        if formulario.is_valid():
            info = formulario.cleaned_data
            skin = Skin(arma=info.get("arma"), skin_pack=info.get("skin_pack"), fecha_creacion=info.get("fecha_creacion"))
            skin.save()
            return redirect("listado_de_skins")
    else:
        formulario = BuscarSkin()  # ← se refiere al formulario también

    return render(request, "home/buscar_skin.html", {"formulario": formulario})


def listado_de_skins(request):
    skins = Skin.objects.all()
    return render(request, "home/listado_de_skins.html", {"skins" : skins})

def detalle_skin(request, skin_en_especifico):
    skin = Skin.objects.get(id=skin_en_especifico)
    return render(request, "home/detalle_skin.html", {"skin": skin})

class VistaDetalleSkin(DetailView):
    model = Skin
    template_name = "home/detalle_skin.html"

class VistaModificarSkin(UpdateView):
    model = Skin
    template_name = "home/modificar_skin.html"
    fields = ["arma", "skin_pack", "fecha_creacion"]
    success_url = reverse_lazy("listado_de_skins")

class VistaEliminarSkin(DeleteView):
    model = Skin
    template_name = "home/eliminar_skin.html"
    success_url = reverse_lazy("listado_de_skins")

