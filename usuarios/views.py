from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistroForm
from .models import Usuario
# Create your views here.

def index(request):
    return HttpResponse("hola desde indexcd..")

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            # Si usas el sistema de autenticación de Django, aquí podrías cifrar la contraseña:
            # usuario.set_password(form.cleaned_data["password"])
            usuario.save()
            # Redirige a la página de login o a otra de éxito
            return redirect('login')
    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form}) #en repositorio esto esta mal


def login(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            usuario = Usuario.objects.get(email=email)
            # Nota: En un entorno real, la contraseña debe estar hasheada y utilizar
            # un método de verificación, como por ejemplo, el método check_password().
            if usuario.password == password:
                # Guardamos el ID del usuario en la sesión para "loguearlo"
                request.session['usuario_id'] = usuario.usuario_id
                request.session['nombre'] = usuario.nombre
                return redirect('libros:index')  # Redirige a la página principal u otra deseada
            else:
                error = "Email o contraseña incorrectos."
        except Usuario.DoesNotExist:
            error = "Email o contraseña incorrectos."
    
    return render(request, 'login.html', {'error': error})
