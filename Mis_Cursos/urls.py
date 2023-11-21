from django.urls import path
from Mis_Cursos import views
urlpatterns = [
    path('', views.inicio),
    path('cargarAlumnos/', views.cargar_alumno, name='cargar_alumnos'),
    path('listarAlumnos/', views.listar_alumnos,name='listar_alumnos'),
    path('modificarAlumno/<int:dni>/', views.modificar_alumno,name='modificar_alumno'),
    path('eliminarAlumno/', views.eliminar_alumno),
    path('asignarCurso/', views.asignar_curso),
     path('alumno/', views.info_alumno, name='info_alumno'),
]