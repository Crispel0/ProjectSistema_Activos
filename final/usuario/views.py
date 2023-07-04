from django.shortcuts import render, redirect
from .forms import UsuarioForm
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required(login_url='login')

def index(request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    return render (request, 'index.html',{'titulo':"Bienvenido", 'rol_usuario':rol_usuario})

#@login_required(login_url='login')
def perfil(request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    titulo = "Usuarios - Perfil"
    usuario = Usuario.objects.get(id=pk)
    form = UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form,
        'rol_usuario':rol_usuario
    }
    return render (request, 'usuario/perfil.html', context)

#@login_required(login_url='login')
def crear_usuario(request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    titulo="Crear-Usuarios"
    if request.method == "POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            if not User.objects.filter(username=request.POST['documento']):
                user = User.objects.create_user('nombre','email@email','pass')
                user.username= request.POST['documento']
                user.first_name= request.POST['nombres']
                user.last_name= request.POST['apellidos']
                user.email= request.POST['email']
                user.password=make_password(request.POST['documento'])
                user.save()
                user_group = User
                #my_group= Group.objects.get(name='Normal')
                #usuario.user.groups.clear()
                #my_group.user_set.add(usuario.user)
            else:
                user=User.objects.get(username=request.POST['documento'])

            usuario= Usuario.objects.create(
                nombres=request.POST['nombres'],
                apellidos=request.POST['apellidos'],
                email=request.POST['email'],
                tipoDocumento=request.POST['tipoDocumento'],
                documento=request.POST['documento'],
                telefono=request.POST['telefono'],
                direccion=request.POST['direccion'],
                fecha_nacimiento=request.POST['fecha_nacimiento'],
                user=user,
                rol=request.POST['rol'],
            )
            return redirect('usuarios')
        else:
            form = UsuarioForm(request.POST)
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'form':form,
        'rol_usuario':rol_usuario

    }
    return render(request,'usuario/crear.html',context)

def usuarios_editar(request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    titulo="Usuarios - Editar"
    usuario= Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST, instance=usuario)
        print (form)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form,
        'usuario':usuario,
        'rol_usuario':rol_usuario,
    }
    return render(request,'usuario/modal.html',context)

def usuarios_eliminar(request, pk): 
    Usuario.objects.filter(id=pk).update(
            estado='1'
        )
    messages.success(request, "Accion realizada correctamente!")
    return redirect('usuarios')
    
    
#@login_required(login_url='login')
def usuarios(request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    listar_usuario=Usuario.objects.all()
    context ={'usuarios':listar_usuario, 'titulo':"Lista Usuarios", 'rol_usuario':rol_usuario}
    return render (request, 'usuario/usuarios.html', context )