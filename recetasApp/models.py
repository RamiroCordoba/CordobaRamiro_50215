from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Historia(models.Model):
    titulo = models.CharField(max_length=70)
    descripcionBreve = models.TextField(max_length=180)
    historia = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fechaPublicacion = models.DateTimeField(default=timezone.now)

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
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    imagenReceta = models.ImageField(blank=True, upload_to="media/")

    class Meta:
        verbose_name = "receta"
        verbose_name_plural = "recetas"
        ordering = ["titulo"]

    # imagen=models.ImageField(upload_to='recetas')
    def __str__(self):
        return f"{self.titulo}"


# _____________ Avatares
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"
