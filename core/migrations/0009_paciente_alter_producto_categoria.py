# Generated by Django 4.0.4 on 2022-05-19 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rango_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('correo', models.CharField(max_length=64, verbose_name='Correo')),
                ('numero', models.CharField(max_length=64, verbose_name='Numero')),
                ('diagnostico', models.CharField(max_length=40, verbose_name='Diagnostico paciente')),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria'),
        ),
    ]