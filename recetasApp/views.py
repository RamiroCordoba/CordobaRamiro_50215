from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# ________________________________ Otras funciones ________________________________#
def home(request):
    return render(request, "recetasApp/index.html")


def sobreNosotros(request):
    return render(request, "recetasApp/about.html")


def paginaNoEncontrada(request):
    return render(request, "recetasApp/error404.html")


# ________________________________ Recetas ________________________________#
# ___________ CRUD de receta
@login_required
def recetas(request):
    contexto = {"recetas": Receta.objects.all().order_by("id")}
    return render(request, "recetasApp/recetas.html", contexto)


@login_required
def recetaCreate(request):
    if request.method == "POST":
        miForm = RecetaForm(request.POST, request.FILES)
        if miForm.is_valid():
            recetaNueva = miForm.save(commit=False)
            recetaNueva.autor = request.user
            recetaNueva.save()
            return redirect(reverse_lazy("recetas"))
    else:
        miForm = RecetaForm()
    return render(request, "recetasApp/recetasForm.html", {"form": miForm})


@login_required
def recetaUpdate(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    if request.method == "POST":
        miForm = RecetaForm(request.POST)
        if miForm.is_valid():
            receta.titulo = miForm.cleaned_data.get("titulo")
            receta.descripcion = miForm.cleaned_data.get("descripcion")
            receta.ingredientes = miForm.cleaned_data.get("ingredientes")
            receta.instrucciones = miForm.cleaned_data.get("instrucciones")
            receta.save()
            return redirect(reverse_lazy("recetas"))

    else:
        miForm = RecetaForm(
            initial={
                "titulo": receta.titulo,
                "descripcion": receta.descripcion,
                "ingredientes": receta.ingredientes,
                "instrucciones": receta.instrucciones,
            }
        )
    return render(request, "recetasApp/recetasForm.html", {"form": miForm})


@login_required
def recetaDelete(request, id_receta):
    receta = Receta.objects.get(id=id_receta)
    receta.delete()
    return redirect(reverse_lazy("recetas"))


# ___________ Busqueda de recetas
@login_required
def buscarRecetas(request):
    return render(request, "recetasApp/buscarReceta.html")


@login_required
def encontrarRecetas(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        recetas = Receta.objects.filter(titulo__icontains=patron)
        contexto = {"recetas": recetas}
        return render(request, "recetasApp/recetas.html", contexto)

    contexto = {"recetas": Receta.objects.all()}
    return render(request, "recetasApp/recetas.html", contexto)


@login_required
def mostrarDetalles(request, id_receta):
    laRreceta = Receta.objects.get(id=id_receta)
    contexto = {"receta": laRreceta}
    return render(request, "recetasApp/recetasDetalle.html", contexto)


# ________________________________ Historias ________________________________#
# ___________ CRUD de historia
@login_required
def historias(request):
    contexto = {"historias": Historia.objects.all().order_by("id")}
    return render(request, "recetasApp/historias.html", contexto)


@login_required
def historiaAmpliada(request, id_historia):
    laHistoria = Historia.objects.get(id=id_historia)
    contexto = {"historia": laHistoria}
    return render(request, "recetasApp/historiaAmpliada.html", contexto)


@login_required
def historiasCreate(request):
    if request.method == "POST":
        miForm = HistoriaForm(request.POST)
        if miForm.is_valid():
            historia_titulo = miForm.cleaned_data.get("titulo")
            historia_historia = miForm.cleaned_data.get("historia")
            historia_descripcionBreve = miForm.cleaned_data.get("descripcionBreve")
            historiaNueva = Historia(
                titulo=historia_titulo,
                historia=historia_historia,
                descripcionBreve=historia_descripcionBreve,
            )
            historiaNueva.autor = request.user
            historiaNueva.save()
            contexto = {"historias": Historia.objects.all()}
            return render(request, "recetasApp/historias.html", contexto)
    else:
        miForm = HistoriaForm()
    return render(request, "recetasApp/historiasForm.html", {"form": miForm})


@login_required
def historiaUpdate(request, id_historia):
    historia = Historia.objects.get(id=id_historia)
    if request.method == "POST":
        miForm = HistoriaForm(request.POST, instance=historia)
        if miForm.is_valid():
            historia.titulo = miForm.cleaned_data.get("titulo")
            historia.descripcionBreve = miForm.cleaned_data.get("descripcionBreve")
            historia.historia = miForm.cleaned_data.get("historia")
            historia.save()
            contexto = {"historias": Historia.objects.all()}
            return render(request, "recetasApp/historias.html", contexto)

    else:
        miForm = HistoriaForm(
            initial={
                "titulo": historia.titulo,
                "historia": historia.historia,
            }
        )

    return render(request, "recetasApp/historiasForm.html", {"form": miForm})


@login_required
def historiaDelete(request, id_historia):
    historia = Historia.objects.get(id=id_historia)
    historia.delete()
    return redirect(reverse_lazy("historias_de_cocina"))


# ___________ Busqueda de historias
@login_required
def buscarHistorias(request):
    return render(request, "recetasApp/buscarHistorias.html")


@login_required
def encontrarHistorias(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        historias = Historia.objects.filter(titulo__icontains=patron)
        contexto = {"historias": historias}
        return render(request, "recetasApp/historias.html", contexto)

    contexto = {"historias": Historia.objects.all()}
    return render(request, "recetasApp/historias.html", contexto)


# ________________________________ Login, logout, Autenticacion, Registro ________________________________#
# __________ Login
def login_request(request):
    if request.method == "POST":
        elUsuario = request.POST["username"]
        laClave = request.POST["password"]
        user = authenticate(request, username=elUsuario, password=laClave)
        if user is not None:
            login(request, user)
            # _________ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            # ________________________________________________________

            return render(request, "recetasApp/index.html")
        else:
            return redirect(reverse_lazy("login"))

    else:
        miForm = AuthenticationForm()
    return render(request, "recetasApp/login.html", {"form": miForm})


# _________ Registro
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy("home"))
    else:
        # __ Si ingresa en el else es la primera vez
        miForm = RegistroForm()

    return render(request, "recetasApp/registro.html", {"form": miForm})


# ________________________________ Edicion de perfil, cambio de contraseña, Avatar ________________________________#
# ______________ Editar perfil
@login_required
def editPorfile(request):
    usuario = request.user

    if request.method == "POST":
        miForm = UserEditForm(request.POST)

        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        # __ Si ingresa en el else es la primera vez
        miForm = UserEditForm(instance=usuario)

    return render(request, "recetasApp/editarPerfil.html", {"form": miForm})


# ______________  Cambiar contraseña
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "recetasApp/cambiar_clave.html"
    success_url = reverse_lazy("home")


# ______________ Agregado de avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            # ___ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            # ____________________________________________________
            avatar = Avatar(user=usuario, imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()

    return render(request, "recetasApp/agregarAvatar.html", {"form": miForm})
