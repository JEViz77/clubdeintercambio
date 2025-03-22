from django.urls import path

from . import views
app_name = "prestamos"
urlpatterns = [
    path("", views.index, name="index"),
     path("solicitar/<int:libro_id>", views.solicitar, name="solicitar"),
    path("aceptar/<int:prestamos_id>", views.aceptar, name="aceptar"),
    path("cancelar/<int:prestamos_id>", views.cancelar, name="cancelar"),
]