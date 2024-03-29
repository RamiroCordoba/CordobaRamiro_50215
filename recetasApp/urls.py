from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # __________ Menu principal __________#
    path("", home, name="home"),
    # __________ Otras paginas __________#
    path("sobre_nosotros/", sobreNosotros, name="sobre_nosotros"),
    path("error/", paginaNoEncontrada, name="error"),
    # __________ Recetas __________#
    path("receta_create/", recetaCreate, name="receta_create"),
    path("recetas/", recetas, name="recetas"),
    path("receta_update/<id_receta>/", recetaUpdate, name="receta_update"),
    path("receta_delete/<id_receta>/", recetaDelete, name="receta_delete"),
    path("buscar_recetas/", buscarRecetas, name="buscar_recetas"),
    path("encontrar_Recetas/", encontrarRecetas, name="encontrar_Recetas"),
    path("receta_detalle/<id_receta>/", mostrarDetalles, name="receta_detalle"),
    # __________ Historias __________#
    path("historias_create/", historiasCreate, name="historias_create"),
    path("historias_de_cocina/", historias, name="historias_de_cocina"),
    path("historia_update/<id_historia>/", historiaUpdate, name="historia_update"),
    path("historia_delete/<id_historia>/", historiaDelete, name="historia_delete"),
    path(
        "historia_ampliada/<id_historia>/", historiaAmpliada, name="historia_ampliada"
    ),
    path("buscar_historias/", buscarHistorias, name="buscar_historias"),
    path("encontrar_historias/", encontrarHistorias, name="encontrar_historias"),
    # __________ Login, logout, Registro __________#
    path("login/", login_request, name="login"),
    path(
        "logout/",
        LogoutView.as_view(template_name="recetasApp/logout.html"),
        name="logout",
    ),
    path("registrar/", register, name="registrar"),
    # __________ Edicion de perfil, cambio de contraseña, Avatar __________#
    path("perfil/", editPorfile, name="perfil"),
    path("<int:pk>/password/", CambiarClave.as_view(), name="cambiar_clave"),
    path("agregar_avatar/", agregarAvatar, name="agregar_avatar"),
]
