from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Historia(models.Model):
    titulo = models.CharField(max_length=70)
    # imagen=models.ImageField(upload_to='historias')
    historia = models.TextField()

    class Meta:
        verbose_name = "historia"
        verbose_name_plural = "historias"
        ordering = ["titulo"]

    # autor=models.ForeignKey('Usuario',on_delete=models.CASCADE,related_name="historias")
    def __str__(self):
        return f"{self.titulo}"


class Receta(models.Model):
    titulo = models.CharField(max_length=70)
    descripcion = models.TextField()
    ingredientes = models.TextField()
    instrucciones = models.TextField()

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ["titulo"]

    # imagen=models.ImageField(upload_to='recetas')
    def __str__(self):
        return f"{self.titulo}"


class Comentario(models.Model):
    opinion = models.TextField()
    # usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # receta=models.ForeignKey(Receta, related_name="comentarios",on_delete=models.CASCADE)

    class Meta:
        verbose_name = "comentario"
        verbose_name_plural = "comentarios"


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre}"


# _____________ Avatares
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
