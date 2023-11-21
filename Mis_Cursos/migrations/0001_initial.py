# Generated by Django 4.2.7 on 2023-11-19 01:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BandaHoraria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('horario_inicio', models.DateTimeField()),
                ('horario_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('nota', models.IntegerField()),
                ('banda_horaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mis_Cursos.bandahoraria')),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('dni', models.IntegerField(unique=True)),
                ('telefono', models.CharField(blank=True, max_length=255)),
                ('correo_electronico', models.EmailField(blank=True, max_length=255)),
                ('curso', models.ManyToManyField(blank=True, to='Mis_Cursos.curso')),
            ],
        ),
    ]
