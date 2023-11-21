from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,JsonResponse, HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from .models import Alumno, Curso
from .forms import CargarAlumnosForm, ModificarAlumnoForm
import csv
import logging
import traceback
import json

logger = logging.getLogger(__name__)

# Create your views here.
def inicio(request):
    return render(request,'index.html')

def cargar_alumno(request):
    if request.method == 'POST':
        form = CargarAlumnosForm(request.POST, request.FILES)
        print(f"Formulario válido: {form.is_valid()}")
        if form.is_valid():
            archivo_csv = request.FILES['archivo_csv']
            archivo_decoded = archivo_csv.read().decode('utf-8').splitlines()

            print("Contenido del archivo CSV:")
            for linea in archivo_decoded:
                print(linea)

            if not archivo_decoded:
                return render(request, 'alumnos/cargado_alumno.html', {'error': 'El archivo está vacío'})

            reader = csv.DictReader(archivo_decoded)

            if 'DNI' not in reader.fieldnames or 'Nombre' not in reader.fieldnames or 'Apellido' not in reader.fieldnames or 'Email' not in reader.fieldnames or 'Curso' not in reader.fieldnames:
                return render(request, 'alumnos/cargado_alumno.html', {'error': 'El archivo CSV debe contener las columnas DNI, Nombre, Apellido, Email y Curso'})

            for fila in reader:
                try:
                    _, created = Alumno.objects.get_or_create(
                        dni=fila['DNI'],
                        defaults={
                            'nombre': fila['Nombre'],
                            'apellido': fila['Apellido'],
                            'telefono': fila.get('Telefono', ''),
                            'correo_electronico': fila.get('Email', ''),
                        }
                    )
                    if created and 'Curso' in fila and fila['Curso']:
                        alumno = Alumno.objects.get(dni=fila['DNI'])
                        curso, _ = Curso.objects.get_or_create(nombre=fila['Curso'])
                        alumno.cursos.add(curso)

                except Exception as e:
                    error_message = f"Error al procesar fila: {fila}\nError: {str(e)}\nTraceback: {traceback.format_exc()}"
        return render(request, 'alumnos/cargado_alumno.html', {'success': 'Alumnos cargados exitosamente'})
        logger.info('Alumnos cargados exitosamente')
    else:
        form = CargarAlumnosForm()

    return render(request, 'alumnos/cargado_alumno.html', {'form': form})


def listar_alumnos(request):
    alumnos=Alumno.objects.all()
    for alumno in alumnos:
        cursos_del_alumno = alumno.cursos.all()
        print(f"Alumno: {alumno.nombre} - Cursos: {[curso.nombre for curso in cursos_del_alumno]}")
    return render(request,'alumnos/listado.html', {'alumnos': alumnos})

def info_alumno(request):
    dni = request.GET.get('dni', None)
    if dni is not None:
        try:
            alumno = Alumno.objects.get(dni=dni)
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{alumno.nombre}_{alumno.apellido}_info.csv"'

            writer = csv.writer(response)
            writer.writerow(['Nombre', 'Apellido', 'DNI', 'Telefono', 'Email', 'Curso', 'Banda Horaria'])
            writer.writerow([alumno.nombre, alumno.apellido, alumno.dni, alumno.telefono, alumno.correo_electronico])
            cursos = alumno.cursos.all()
            
            for curso in cursos:               
                banda_horaria_nombre = curso.banda_horaria.nombre if curso.banda_horaria else ''

                writer.writerow([alumno.nombre, alumno.apellido, alumno.dni, alumno.telefono,
                                 alumno.correo_electronico, curso.nombre, banda_horaria_nombre])

            return response
        except Alumno.DoesNotExist:
            return HttpResponse('Alumno no encontrado', status=404)
    else:
        return HttpResponse('Se requiere el parámetro "dni"', status=400)

@csrf_exempt 
@require_http_methods(["PUT", "POST"])
def modificar_alumno(request,dni):
    alumno = get_object_or_404(Alumno, dni=dni)
    if request.method == 'POST' or request.headers.get('X-HTTP-Method-Override') == 'PUT':
        try:
            data = json.loads(request.body)
            form = ModificarAlumnoForm(data, instance=alumno)
            if form.is_valid():
                form.save()
                return JsonResponse({'message': 'Alumno actualizado correctamente'})
            else:
                return JsonResponse({'error': form.errors}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponseNotAllowed(['PUT', 'POST'], 'Method not allowed')

def eliminar_alumno(request):
    return render(request,'alumnos/eliminar_alumno.html')

def busqueda_alumno(request):
    return render(request,'alumnos/busqueda_alumno.html')

def asignar_curso(request):
    return render(request,'cursos/asignar_curso.html')

