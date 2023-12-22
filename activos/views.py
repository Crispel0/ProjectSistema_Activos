from django.shortcuts import render, redirect
from django.template import RequestContext
from .forms import TipoActivoForm, InformacionSoftwareForm, InformacionHardwareForm, SistemaOperativoForm, VersionSistemaOperativoForm, OfimaticaForm,VersionOfimaticaForm
from .models import TipoActivo,InformacionSoftware, Antivirus,InformacionHardware,Navegador ,HerramientaCloud, SistemaOperativo,VersionSistemaOperativo, Ofimatica, VersionOfimatica
from django.http import HttpResponse
from .utils import render_to_pdf
from django.views.generic import View
from usuarios.models import Usuario
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.
def listado_activos(request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    if request.method == 'POST':
        nuevo_activo_form = TipoActivoForm(request.POST)
        if nuevo_activo_form.is_valid():
            nuevo_activo = nuevo_activo_form.save(commit=False)
            nuevo_activo.usuario_registra = request.user.usuario
            nuevo_activo.save()
        return redirect (listado_activos)
    else:  
        consulta_activos = TipoActivo.objects.all()
        consulta_software = InformacionSoftware.objects.all()
        formulario_activo = TipoActivoForm()
        titulo = "Activos"
        context = {'consulta_activos':consulta_activos, 'consulta_software':consulta_software, 'form':formulario_activo, 'titulo':titulo, 'rol_usuario':rol_usuario}
        return render (request, 'activo/listado_activos.html', context)
    
def informacion_software(request, id):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    if request.method == 'POST':
        info_software = InformacionSoftwareForm(request.POST)
        if info_software.is_valid():
            tipo_activo = TipoActivo.objects.get(id=id)
            new_info_software = InformacionSoftware.objects.filter(id_activo=tipo_activo).first()
            if new_info_software:
                new_info_software.usuario_registro =  new_info_software.usuario_registro
                new_info_software.id_activo = new_info_software.id_activo
                new_info_software.user = request.user
                new_info_software.user =True
                new_info_software.id_activo.id = new_info_software.id_activo.id
                new_info_software.save()
                
               
            else:
                nueva_info_software = info_software.save(commit=False)
                tipo_activo = TipoActivo.objects.get(id=id)
                nueva_info_software.id_activo = tipo_activo
                nueva_info_software.usuario_registro = rol_usuario  
                nueva_info_software.user = request.user
                nueva_info_software.registrado = True
                nueva_info_software.save()
                tipo_activo.estado_software = True
                tipo_activo.save()

        return redirect('listado_activos')
    
    else: #here is necessary change the code
        tipo_activo = TipoActivo.objects.get(id=id)
        existing_info_software = InformacionSoftware.objects.filter(id_activo=tipo_activo).first()
        formulario = InformacionSoftwareForm(instance=existing_info_software)

        
        titulo = "Información de software"
        consulta = TipoActivo.objects.filter(id=id)
        context = {'form': formulario, 'titulo': titulo, 'consulta': consulta, 'rol_usuario':rol_usuario}
        return render(request, 'activo/informacion_software.html', context)

def informacion_hardware(request, id):
    context = {
        'form':InformacionHardwareForm()
    }

    if request.method == 'POST':
        form = InformacionHardwareForm(request.POST)

        if form.is_valid():
            context['message'] = "Formulario Guardado"
            print("POST - FORMULARIO - OK")
            form.save()
            return render(request, 'activo/informacion_hardware.html', context)

        else:
            context['form'] = form
            context['message'] = "Formulario Invalido"
            return render(request, 'activo/informacion_hardware.html', context)

    if request.method == 'GET':
        print("GET - FORMULARIO - OK")
        return render(request, 'activo/informacion_hardware.html', context)

def administar_software(request):
    
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    sistemas_operativos = SistemaOperativo.objects.filter(estado=True)
    versiones_sistemas_operativos = VersionSistemaOperativo.objects.filter(estado=True)

    context = {
        'titulo':"Administar software",
        'sistemas_operativos':sistemas_operativos,
        'versiones_sistemas_operativos':versiones_sistemas_operativos,
        'rol_usuario':rol_usuario
    }
    return render (request, 'administrador/administar_sistemas_operativos.html',context)

def agregar_sistema_operativo (request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    
    if request.method == 'GET':
        form = SistemaOperativoForm()
    else:
        sistema = SistemaOperativoForm(request.POST)
        if sistema.is_valid():
            sistema.save()
        return redirect ('administar_software')
    context = {'titulo':"Agregar sistema operativo", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Agregar Sistema operativo"}
    return render (request, 'administrador/agregar_sistema_operativo.html',context)

def editar_sistema_operativo (request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    sistema_operativo =  SistemaOperativo.objects.select_related().get(id=pk)
    print(sistema_operativo)
    sistema = SistemaOperativo.objects.get(id=pk)
    if request.method == "POST":
        form= SistemaOperativoForm(request.POST, instance=sistema)
        if form.is_valid():
            form.save()
            return redirect('administar_software')
    else:
        form= SistemaOperativoForm(instance=sistema)
    context = {'titulo':"Editar sistema operativo", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Editar sistema operativo"}
    return render (request, 'administrador/agregar_sistema_operativo.html',context)

def eliminar_sistema_operativo(request,pk): 
    SistemaOperativo.objects.filter(id=pk).update(
            estado='False'
        )
    mensaje = messages.success(request, "Accion realizada correctamente!")
    print(mensaje)
    return redirect('administar_software')


def agregar_version_sistema_operativo (request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    if request.method == 'GET':
        form = VersionSistemaOperativoForm()
    else:
        sistema = VersionSistemaOperativoForm(request.POST)
        sistema.save()
        return redirect ('administar_software')
    context = {'titulo':"Agregar versión de sistema operativo", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Agregar Versión sistema operativo"}
    return render (request, 'administrador/agregar_version_sistema_operativo.html',context)

def editar_version_sistema_operativo (request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    version = VersionSistemaOperativo.objects.get(id=pk)
    if request.method == "POST":
        form= VersionSistemaOperativoForm(request.POST, instance=version)
        if form.is_valid():
            form.save()
            return redirect('administar_software')
    else:
        form= VersionSistemaOperativoForm(instance=version)
    context = {'titulo':"Editar sistema operativo", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Editar versión de sistema operativo"}
    return render (request, 'administrador/agregar_version_sistema_operativo.html',context)

def eliminar_version_sistema_operativo(request, pk): 
    VersionSistemaOperativo.objects.filter(id=pk).update(
            estado='False'
        )
    messages.success(request, "Accion realizada correctamente!")
    return redirect('administar_software')

def administrar_ofimatica (request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    ofimatica = Ofimatica.objects.all()
    version_ofimatica = VersionOfimatica.objects.all()
    context = {
        'titulo':"Ofimatica",
        'ofimatica':ofimatica,
        'version_ofimatica':version_ofimatica,
        'rol_usuario':rol_usuario
    }
    return render (request, 'administrador/administar_paquete_ofimatica.html', context)

def agregar_paquete_ofimatica (request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    if request.method == 'GET':
        form = OfimaticaForm()
    else:
        sistema = OfimaticaForm(request.POST)
        if sistema.is_valid:
            sistema.save()
        return redirect ('administrar_paquete_ofimatica')
    context = {'titulo':"Agregar Paquete ofimatica", 'form':form, 'rol_usuario':rol_usuario}
    return render (request, 'administrador/agregar_paquete_ofimatica.html', context)

def editar_paquete_ofimatica (request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    
    ofimatica = Ofimatica.objects.get(id=pk)
    if request.method == "POST":
        form= OfimaticaForm(request.POST, instance=ofimatica)
        if form.is_valid():
            form.save()
            return redirect('administrar_paquete_ofimatica')
    else:
        form= OfimaticaForm(instance=ofimatica)
    context = {'titulo':"Editar Paquete Ofimatica", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Editar paquete Ofimatica"}
    return render (request, 'administrador/agregar_paquete_ofimatica.html',context)

def eliminar_paquete_ofimatica(request, pk): 
    Ofimatica.objects.filter(id=pk).update(
            estado='False'
        )
    messages.success(request, "Accion realizada correctamente!")
    return redirect('administrar_paquete_ofimatica')

def editar_version_paquete_ofimatica (request, pk):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    
    ofimatica = VersionOfimatica.objects.get(id=pk)
    if request.method == "POST":
        form= VersionOfimaticaForm(request.POST, instance=ofimatica)
        if form.is_valid():
            form.save()
            return redirect('administrar_paquete_ofimatica')
    else:
        form= OfimaticaForm(instance=ofimatica)
    context = {'titulo':"Editar Paquete Ofimatica", 'form':form, 'rol_usuario':rol_usuario, 'titulo_vista':"Editar paquete Ofimatica"}
    return render (request, 'administrador/agregar_version_ofimatica.html',context)

def eliminar_version_paquete_ofimatica(request, pk): 
    VersionOfimatica.objects.filter(id=pk).update(
            estado='False'
        )
    messages.success(request, "Accion realizada correctamente!")
    return redirect('administrar_paquete_ofimatica')

def agregar_version_ofimatica (request):
    rol_usuario = Usuario.objects.filter (user = request.user.id).first() 
    if request.method == 'GET':
        form = VersionOfimaticaForm()
    else:
        version = VersionOfimaticaForm(request.POST)
        if version.is_valid():
            version.save()
        return redirect ('administrar_paquete_ofimatica')
    context = {'titulo':"Agregar versión ofimatica", 'form':form, 'rol_usuario':rol_usuario}
    return render (request, 'administrador/agregar_version_ofimatica.html',context)

class generar_pdf(View):
    def get(request,self,pk):
        
        print(f"pri.key:{pk}")
        
        activo = TipoActivo.objects.get(id=pk)
    
        software = InformacionSoftware.objects.get(id=pk)
        hardware = InformacionHardware.objects.get(id=pk)
        
        version_sistema_operativo = VersionSistemaOperativo.objects.all()
        version_ofimatica = VersionOfimatica.objects.get(id=pk)
        antivirus = Antivirus.objects.get(id=pk)
        herramienta_cloud = HerramientaCloud.objects.get(id=pk)
        navegador = Navegador.objects.get(id=pk)
        ofimatica = Ofimatica.objects.get(id=pk)
        
        template_name="activo/informacion_activo.html"
        
        data = {
                'activo': activo,
                'informacion_software':software,
                'version_sistema_op' :version_sistema_operativo,
                'version_ofimatica' : version_ofimatica,
                'cloud':herramienta_cloud,
                'antivirus': antivirus,
                'navegador':navegador,
                'ofimatica':ofimatica,
                'informacion_hardware': hardware
            }      
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type='application/pdf')

