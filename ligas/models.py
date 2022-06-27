from tkinter import Widget
from django.db import models

class Ligas(models.Model):
    torneo = models.CharField(max_length=40)
    equipos = models.IntegerField()
    internacional = models.BooleanField()
    descripcion = models.TextField(blank = True, null=True)

    def __str__(self):
        es_internacional = 'Si' if self.internacional else 'No'
        return f'Torneo: {self.torneo} \nInternacional: {es_internacional}'

