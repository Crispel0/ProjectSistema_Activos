from django.urls import path
from .views import index, crear_usuario, perfil, usuarios, usuarios_editar

urlpatterns = [
    path("inicio/", index, name="index"),
    path("crear_usuario/",crear_usuario, name="crear_usuario"),
    path("perfil/<int:pk>/", perfil, name="perfil"),
    path("usuarios/", usuarios,name="usuarios"),
    path("usuarios_editar/<int:pk>/", usuarios_editar, name="editar_usuario")
    
]
