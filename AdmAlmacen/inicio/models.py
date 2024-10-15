from django.db import models

# Create your models here.
from django.db import models

class Almacen(models.Model):
    descripcion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion