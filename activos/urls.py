from django.urls import path
from . import views
from .views import  listado_activos, informacion_hardware,administar_software, agregar_sistema_operativo, agregar_version_sistema_operativo, administrar_ofimatica,agregar_paquete_ofimatica,editar_paquete_ofimatica,eliminar_paquete_ofimatica, agregar_version_ofimatica,editar_version_paquete_ofimatica, generar_pdf, editar_sistema_operativo,eliminar_sistema_operativo, eliminar_version_sistema_operativo,eliminar_version_paquete_ofimatica,editar_version_sistema_operativo

urlpatterns = [
    path("listado/", listado_activos, name="listado_activos"),
    path("informacion_software/<int:id>", views.informacion_software, name="informacion_software"),
    path("informacion_hardware/<int:id>", informacion_hardware, name="informacion_hardware"),

    path("administrar_software/", administar_software, name="administar_software"),
    path("administar_software/", administar_software, name="administar_software"),
    path("administrar_software/agregar_sistema_operativo/", agregar_sistema_operativo, name="agregar_sistema_operativo"),
    path("administrar_software/agregar_sistema_operativo/<int:pk>", editar_sistema_operativo, name="agregar_sistema_operativo"),
    path ("administrar_software/agregar_version_sistema_operativo/", agregar_version_sistema_operativo, name="agregar_version_sistema_operativo"),
    path ("administar_software/agregar_version_sistema_operativo/<int:pk>",editar_version_sistema_operativo, name="editar_version_sistema_operativo"),
    path ('administrar_software/agregar_version_sistema_operativo/<int:pk>',agregar_version_sistema_operativo, name="agregar_version_sistema_operativo"),
    path ('administrar_software/eliminar_version_sistema_operativo/<int:pk>', eliminar_version_sistema_operativo, name="eliminar_version_sistema_operativo"),
    
    path("administrar_ofimatica/", administrar_ofimatica, name="administrar_paquete_ofimatica"),
    path("administrar_ofimatica/agregar_paquete_ofimatica/", agregar_paquete_ofimatica, name="agregar_paquete_ofimatica"),
    path("administrar_ofimatica/agregar_paquete_ofimatica/<int:pk>", editar_paquete_ofimatica, name="editar_paquete_ofimatica"),
    path("administrar_ofimatica/eliminar_paquete_ofimatica/<int:pk>", eliminar_paquete_ofimatica, name="eliminar_paquete_ofimatica"),
    path("administrar_ofimatica/agregar_version_ofimatica/", agregar_version_ofimatica, name="agregar_version_ofimatica"),
    path("administrar_ofimatica/agregar_version_ofimatica/<int:pk>", editar_version_paquete_ofimatica, name="editar_version_paquete_ofimatica"),

    path("generar_pdf/<pk>", generar_pdf.as_view(), name='generar_pdf'),
    path ('administrar_software/eliminar_sistema_operativo/<int:pk>', eliminar_sistema_operativo, name = "eliminar_sistema_operativo"),
    path("administrar_ofimatica/eliminar_version_ofimatica/<int:pk>", eliminar_version_paquete_ofimatica, name="eliminar_version_paquete_ofimatica"),
]
