# Generated by Django 4.2.6 on 2023-11-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_infomiembros_telefono_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConductasASeguir',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=80)),
            ],
        ),
    ]
