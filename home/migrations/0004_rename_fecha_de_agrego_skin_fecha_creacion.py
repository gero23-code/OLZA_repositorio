# Generated by Django 5.2 on 2025-05-01 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_skin_fecha_de_agrego'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skin',
            old_name='fecha_de_agrego',
            new_name='fecha_creacion',
        ),
    ]
