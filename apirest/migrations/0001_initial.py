# Generated by Django 3.2.8 on 2021-11-03 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('razonsocial', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('ruc', models.CharField(max_length=11)),
                ('celular', models.CharField(max_length=9)),
                ('web', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
