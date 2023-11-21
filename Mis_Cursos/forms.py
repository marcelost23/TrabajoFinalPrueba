from django import forms

class CargarAlumnosForm(forms.Form):
    archivo_csv = forms.FileField(
        label='Seleccionar archivo CSV',
        help_text='Solo se permiten archivos CSV.'
    )
    def limpiar_archivo_csv(self):
        archivo = self.cleaned_data.get('archivo_csv')
        if archivo:
            if not archivo.name.endswith('.csv'):
                raise forms.ValidationError('El archivo debe tener la extensión CSV.')
        return archivo

class ModificarAlumnoForm(forms.Form):
    nombre = forms.CharField(max_length=255, required=False)
    apellido = forms.CharField(max_length=255, required=False)
    telefono = forms.CharField(max_length=255, required=False)
    correo_electronico = forms.EmailField(max_length=255, required=False)