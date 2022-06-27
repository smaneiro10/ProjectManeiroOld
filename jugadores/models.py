from tkinter import Widget
from django.db import models


class Jugadores(models.Model):
    nombre = models.CharField(max_length=40)
    equipo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    descripcion = models.TextField(blank = True, null=True)
    
    def __str__(self):
        return f'Jugador: {self.nombre}'