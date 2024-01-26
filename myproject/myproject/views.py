from django.shortcuts import render
from myproject.models import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    return render(request,'index.html',{
    })


def login_view(request): 
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        passw = request.POST.get('passw')

        user = authenticate(usuario=usuario, passw=passw)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.usuario))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
                                
    return render(request,'login.html',{    
     })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesion cerrada exitosamente')
    return redirect('login')
    

def registro(request):
    return render(request,'registro.html',{
            
    })

              