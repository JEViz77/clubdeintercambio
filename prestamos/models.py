from django.db import models
from usuarios.models import Usuario
from libros.models import Libro

class Estado(models.Model):
    estado_id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion

class Prestamo(models.Model):
    prestamos_id = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='prestamos')
    # Usuario que solicita el préstamo
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"Préstamo {self.prestamos_id} - {self.libro.titulo}"
