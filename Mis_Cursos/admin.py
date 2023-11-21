from django.contrib import admin
from .models import Alumno,Curso,BandaHoraria

class AlumnoAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','dni')
    
class CursoAdmin(admin.ModelAdmin):
    list_display=('nombre','descripcion')

class BandaHorariaAdmin(admin.ModelAdmin):
    list_display=('nombre',)

# Register your models here.
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(BandaHoraria,BandaHorariaAdmin)