from django.contrib.auth import logout
from django.shortcuts import redirect,render
from activos.models import Estado
from json import dumps

def salir(request):
    logout(request)
    return redirect('login')

def panel_personalizado(request):
    total = Estado.objects.all().count()
    estados_activos = Estado.objects.filter(estado = "Activo").count()
    estados_inactivos = Estado.objects.filter(estado = "Inactivo").count()

    data = {
        "total" : total,
        "estados_activos" : estados_activos,
        "estados_inactivos" : estados_inactivos
    }

    dataJson = dumps(data)
    print(dataJson)
    return render(request, 'panel/panel_admin.html', {'data':dataJson})