# Generated by Django 4.2.5 on 2024-03-29 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recetasApp', '0008_receta_autor_receta_imagenreceta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
        migrations.AddField(
            model_name='historia',
            name='autor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
