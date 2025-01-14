# Generated by Django 2.2.4 on 2021-07-26 23:06

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfdi', '0012_auto_20210520_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='descargacfdi',
            name='pac',
            field=models.IntegerField(choices=[(1, 'Miguelito'), (2, 'Prodigia')], default=2),
        ),
        migrations.AlterField(
            model_name='descargacfdi',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendiente de enviar'), (2, 'Pendiente de consultar'), (3, 'Sigue pendiente'), (4, 'Finalizado'), (5, 'Error al consultar solicitud descarga')], default=1),
        ),

        migrations.RunSQL(
            "ALTER TABLE cfdi_descargacfdi ALTER COLUMN pac SET DEFAULT 2"
        ),
    ]
