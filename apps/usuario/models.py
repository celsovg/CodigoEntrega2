from django.db import models
from django.utils import timezone
from apps.producto.models import zapatilla

# Create your models here.


class persona(models.Model):
    id_persona = models.IntegerField(primary_key=True)
    nombre = models. CharField(max_length=20)
    apellido = models. CharField(max_length=20)
    fecha_nacimiento = models.DateField
    telefono = models.CharField(max_length=12)
    email = models.EmailField(max_length=70)
    domicilio = models.CharField(max_length=100)


class compra (models.Model):
    id_compra = models.IntegerField(primary_key=True)
    producto = models.ForeignKey(
        zapatilla, null=True, blank=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField
    fecha_compra = models.DateField (null=True) 
    hora_compra = models.TimeField (null=True)
    persona = models.ForeignKey (
        persona, null=True, blank=True, on_delete=models.CASCADE)

