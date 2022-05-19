# Generated by Django 4.0.4 on 2022-05-19 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='hola', max_length=20, verbose_name='Descripcion remedio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(default='hola', max_length=20, verbose_name='Laboratorio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.CharField(default=23, max_length=20, verbose_name='stock'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Remedio',
        ),
    ]
