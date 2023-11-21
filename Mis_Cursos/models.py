from django.db import models

# Create your models here.
class BandaHoraria(models.Model):
    nombre=models.CharField(max_length=255)
    horario_inicio=models.DateTimeField()
    horario_fin=models.DateTimeField()

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name="Banda Horaria"
        verbose_name_plural="Bandas Horarias"


class Curso(models.Model):
    nombre=models.CharField(max_length=255)
    descripcion=models.CharField(blank=True, null=True, max_length=255)
    banda_horaria=models.ForeignKey('BandaHoraria',on_delete=models.CASCADE)
    nota=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
   

class Alumno(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    dni=models.IntegerField(unique=True)
    telefono=models.CharField(max_length=255,blank=True)
    correo_electronico=models.EmailField(max_length=255,blank=True)
    cursos=models.ManyToManyField('Curso',blank=True)

    def __str__(self) -> str:
        return self.nombre+" "+self.apellido