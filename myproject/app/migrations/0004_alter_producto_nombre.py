# Generated by Django 5.1.3 on 2024-11-07 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_producto_descripcion_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(help_text='introdusca solo valores de caracteres', max_length=100, verbose_name='Nombre : '),
        ),
    ]
