# Generated by Django 4.2.6 on 2024-01-01 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_psillamadas_cedula_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='psillamadas',
            old_name='cedula_usuario',
            new_name='documento',
        ),
    ]
