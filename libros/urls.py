from django.urls import path

from . import views

app_name = 'libros'
urlpatterns = [
    path("", views.index, name="index"),
    path("alta_libro", views.alta_libro, name="alta_libro"),
    path("borrar/<int:libro_id>", views.borrar, name="borrar"),
    path("ver/<int:libro_id>", views.ver, name="ver"),
    
]