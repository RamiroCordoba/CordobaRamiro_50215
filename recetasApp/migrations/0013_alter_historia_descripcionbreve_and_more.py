# Generated by Django 4.2.5 on 2024-03-29 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasApp', '0012_alter_receta_imagenreceta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='descripcionBreve',
            field=models.TextField(max_length=180),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagenReceta',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
