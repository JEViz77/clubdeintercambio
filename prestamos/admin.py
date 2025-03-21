from django.contrib import admin
from .models import Prestamo, Estado


class EstadoAdmin(admin.ModelAdmin):
    list_display = ('estado_id', 'descripcion')
    list_display_links = ('estado_id',)

admin.site.register(Prestamo)
admin.site.register(Estado,EstadoAdmin)

# Register your models here.
