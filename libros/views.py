from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
from prestamos.models import Prestamo, Estado


def index(request):
    if(request.session.get('usuario_id')): 
        libros = Libro.objects.filter(usuario_id=request.session.get('usuario_id'))
        return render(request, 'index.html', {'libros': libros}) 
    else:
        #redirijo a la pagina de login
        return redirect('usuarios:login')

def alta_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.usuario_id = request.session.get('usuario_id')
            form.save()
            return redirect('libros:index')  # Redirige a la lista de libros, por ejemplo.
    else:
        form = LibroForm()
    return render(request, 'alta_libro.html', {'form': form})

def borrar(request, libro_id):
    libro = Libro.objects.get(libro_id=libro_id)
    libro.delete()
    return redirect('libros:index')
  
def ver(request, libro_id):
    libro = Libro.objects.get(libro_id=libro_id)
    prestamos = libro.prestamos.all()
    return render(request, 'ver.html', {'libro': libro, 'prestamos': prestamos})