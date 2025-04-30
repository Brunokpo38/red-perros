from django.db import models

class PerroPerdido(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    zona = models.CharField(max_length=100)
    fecha = models.DateField(auto_now_add=True)
    imagen = models.ImageField(upload_to='perros/', blank=True, null=True)

    def __str__(self):
        return self.nombre
