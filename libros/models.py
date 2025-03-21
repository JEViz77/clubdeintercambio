from django.db import models
from usuarios.models import Usuario  # Importamos el modelo Usuario

class Libro(models.Model):
    libro_id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='libros/media')
    descripcion = models.TextField()
    # Relación: cada libro pertenece a un usuario
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    #relacion libro prestamo
   
    def __str__(self):
        return self.titulo


# Create your models here.