from django.contrib.auth import logout
from django.shortcuts import redirect,render
from activos.models import Estado,Activo,VersionSistemaOperativo,InformacionHardware, InformacionSoftware
from django.contrib.auth.models import User

import json

def salir(request):
    logout(request)
    return redirect('login')

def panel_personalizado(request):
    
    cantidad_version_so = VersionSistemaOperativo.objects.values_list("id",flat=True).count() # cantidad total versiones quantity amount versions
    cantidad_version_so_activo = VersionSistemaOperativo.objects.values_list("estado", flat=True).filter(estado=True).count() # cantidad de versiones activas quantity versions active
    cantidad_version_so_inactivo = VersionSistemaOperativo.objects.values_list("estado", flat=True).filter(estado=False).count() #cantidad versiones inactivas quantity versions inactive

    cantidad_registros_hardware = InformacionHardware.objects.values_list("id", flat=True).count()
    cantidad_registros_software = InformacionSoftware.objects.values_list("id",flat=True).count()

    cantidad_usuarios_registrados = User.objects.values_list("id", flat=True).count()
    cantidad_usuarios_activos = User.objects.filter(is_active = 1).count()
    cantidad_usuarios_inactivos = User.objects.filter(is_active = 0).count()
    cantidad_usuarios_staff = User.objects.filter(is_staff = 1).count()

    data = {
        #versiones sistemas_operativos_cantidad_activos_e_inactivos
        "version_s_operativo_id": cantidad_version_so,
        "version_so_activo": cantidad_version_so_activo,
        "version_so_inactivo": cantidad_version_so_inactivo,
        #software and hardware
        "cantidad_registros_hardware": cantidad_registros_hardware,
        "cantidad_registros_software": cantidad_registros_software,
        #informacion usuarios
        "cantidad_usuarios_registrados": cantidad_usuarios_registrados,
        "cantidad_usuarios_activos":cantidad_usuarios_activos,
        "cantidad_usuarios_inactivos":cantidad_usuarios_inactivos,
        "cantidad_usuarios_staff":cantidad_usuarios_staff
    }
    
    
    info_panel = json.dumps(data)

    return render(request, 'panel/panel_admin.html',{'info_panel':info_panel})
    