from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=20)
    fecha_fabricacion = models.DateField()
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"