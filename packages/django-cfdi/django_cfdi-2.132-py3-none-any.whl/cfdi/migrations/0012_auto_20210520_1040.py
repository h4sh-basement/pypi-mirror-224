# Generated by Django 3.1.3 on 2021-05-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfdi', '0011_descargacfdi_tipo_solicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cfdi',
            name='fin_conexion_pac',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cfdi',
            name='fin_timbrado',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cfdi',
            name='inicio_conexion_pac',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='cfdi',
            name='inicio_timbrado',
            field=models.DateTimeField(null=True),
        ),
    ]
