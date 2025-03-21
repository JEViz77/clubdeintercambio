from django.db import models


class Usuario(models.Model):
    # Django crea automáticamente un id autoincremental llamado 'id' 
    # pero si deseas llamarlo usuario_id, puedes hacerlo explícito:
    usuario_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # "pass" es palabra reservada en Python
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre