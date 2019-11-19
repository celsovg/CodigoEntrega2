from django import froms

from apps.usuario.models import usuario

class UsuarioForm(forms.modelForm)

class Meta:
    model = Usuario

fields = [
'id_persona',
'nombre',
'apellido',
'fecha_nacimiento',
'telefono',
'email',
'domicilio',
]

labels = {
'id_persona': 'Id_persona',
'nombre': 'Nombre',
'apellido': 'Apellido',
'fecha_nacimiento':'Fecha nacimiento',
'telefono': 'Telefono',
'email': 'Email',
'domicilio':'Domicilio',
}

widgets = {
'id_persona': forms.TextInput(attrs={'class': 'form-control'}),
'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
'apellido': forms.TextInput(attrs={'class': 'form-control'}),
'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control'}),
'telefono': forms.TextInput(attrs={'class': 'form-control'}),
'email': forms.TextInput(attrs={'class': 'form-control'}),
'domicilio': forms.TextInput(attrs={'class': 'form-control'}),
}