# Generated by Django 4.0.4 on 2022-05-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_producto_estado_alter_producto_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('idRango', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Rango')),
                ('nombreRango', models.CharField(max_length=50, verbose_name='Nombre deL Rango')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Rut', models.CharField(max_length=9, primary_key=True, serialize=False, verbose_name='Rut ')),
                ('Contra', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('Nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('Apellidos', models.CharField(max_length=60, verbose_name='Apellidos')),
                ('Mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('Telefono', models.IntegerField(verbose_name='Teléfono')),
                ('Direccion', models.CharField(max_length=300, verbose_name='Dirección')),
            ],
        ),
    ]