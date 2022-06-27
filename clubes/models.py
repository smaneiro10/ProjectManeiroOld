from django.db import models

class Clubes(models.Model):
    nombre = models.CharField(max_length=30)
    provincia = models.CharField(max_length=30)
    descripcion = models.TextField(blank = True, null=True)

    def __str__(self):
        return f'Club: {self.nombre} \nProvincia: {self.provincia}'
