from django.contrib import admin
from .models import *


# Register your models here.
class RecetaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "descripcion")


admin.site.register(Receta, RecetaAdmin)
admin.site.register(Historia)
