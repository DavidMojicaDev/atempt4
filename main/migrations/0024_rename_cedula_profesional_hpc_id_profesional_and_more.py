# Generated by Django 4.2.6 on 2023-11-28 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_hpc_acontecimientos_estresantes_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hpc',
            old_name='cedula_profesional',
            new_name='id_profesional',
        ),
        migrations.RemoveField(
            model_name='hpc',
            name='cond_a_seguir',
        ),
        migrations.AlterField(
            model_name='infomiembros',
            name='id_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='rhpcsituacioncontacto',
            name='id_asesoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpc'),
        ),
        migrations.AlterField(
            model_name='rhpcsituacioncontacto',
            name='id_situacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpcsituacioncontacto'),
        ),
        migrations.AlterField(
            model_name='rhpctiposdemandas',
            name='id_asesoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpc'),
        ),
        migrations.AlterField(
            model_name='rhpctiposdemandas',
            name='id_tipo_demanda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpctiposdemandas'),
        ),
        migrations.AlterField(
            model_name='rhpctiposrespuestas',
            name='id_asesoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpc'),
        ),
        migrations.AlterField(
            model_name='rhpctiposrespuestas',
            name='id_respuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hpctiposrespuestas'),
        ),
        migrations.AlterField(
            model_name='spaactuales',
            name='id_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.infopacientes'),
        ),
        migrations.AlterField(
            model_name='spaactuales',
            name='id_sustancia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.spa'),
        ),
        migrations.CreateModel(
            name='RHPCConductasASeguir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_asesoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.infopacientes')),
                ('id_conducta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.conductasaseguir')),
            ],
        ),
    ]
