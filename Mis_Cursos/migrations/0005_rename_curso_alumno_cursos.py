# Generated by Django 4.2.7 on 2023-11-20 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mis_Cursos', '0004_alter_curso_nota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='curso',
            new_name='cursos',
        ),
    ]
