"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.contrib.auth import views as auth_views
from .views import salir




urlpatterns = [
    path('admin/' , admin.site.urls),
    path('usuario/',include('usuarios.urls')),
    path('activo/',include('activos.urls')),
    path('',auth_views.LoginView.as_view(),name='login'),
    path('', include('django.contrib.auth.urls')),
    path('reiniciar/',auth_views.PasswordResetView.as_view(),name='pass_reset'),
    path('reiniciar/<uid64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reiniciar/completo',auth_views.PasswordResetCompleteView.as_view(),name='password_change_recovery'),
    path('reiniciar/cambiado',auth_views.PasswordResetConfirmView.as_view(),name='password_change_process'),
    path('reiniciar/cambiado/done',auth_views.PasswordResetDoneView.as_view(),name='password_change_done'),
    path("salir/", salir, name='salir')
]

