from django.urls import path
from .views import listado_activos, informacion_software,cargar_versiones, informacion_hardware,administar_software, agregar_sistema_operativo, agregar_version_sistema_operativo, administrar_ofimatica, visualizacion_software_hardware ,agregar_paquete_ofimatica, agregar_version_ofimatica, generar_pdf, editar_sistema_operativo,eliminar_sistema_operativo, eliminar_version_sistema_operativo, editar_version_sistema_operativo

urlpatterns = [
    path("listado/", listado_activos, name="listado_activos"),
    path("informacion_software/<int:id>", informacion_software, name="informacion_software"),
    path("informacion_hardware/<int:id>", informacion_hardware, name="informacion_hardware"),
    path("adminsitar_software/", administar_software, name="administar_software"),
    path("adminsitar_software/agregar_sistema_operativo/", agregar_sistema_operativo, name="agregar_sistema_operativo"),
    path ("administrar_software/agregar_version_sistema_operativo/", agregar_version_sistema_operativo, name="agregar_version_sistema_operativo"),
    path("adminsitar_ofimatica/", administrar_ofimatica, name="administrar_paquete_ofimatica"),
    path("administrar_ofimatica/agregar_paquete_ofimatica/", agregar_paquete_ofimatica, name="agregar_paquete_ofimatica"),
    path("administrar_ofimatica/agregar_version_ofimatica/", agregar_version_ofimatica, name="agregar_version_ofimatica"),
    path ("editar_sistema_operativo/<int:pk>", editar_sistema_operativo, name="editar_sistema_operativo"),
    path('generar_pdf/', generar_pdf.as_view(), name='generar_pdf'),
    path ('eliminar_sistema_operativo/<int:pk>', eliminar_sistema_operativo, name = "eliminar_sistema_operativo"),
    path ('eliminar_version_sistema_operativo/<int:pk>', eliminar_version_sistema_operativo, name="eliminar_version_sistema_operativo"),
    path ('editar_version_sistema_operativo/<int:pk>', editar_version_sistema_operativo, name="editar_version_sistema_operativo"),
    path ('software_hardware/', visualizacion_software_hardware, name="visualizar_software_hardware"),
    path('informacion_software/ajax/cargador_versiones',cargar_versiones, name="ajax_cargador_versiones")


]
