# Generated by Django 4.2.5 on 2024-03-23 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetasApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('historia', models.TextField()),
            ],
        ),
    ]
