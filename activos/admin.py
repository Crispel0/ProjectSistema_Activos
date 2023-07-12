from django.contrib import admin
from .models import Activo,Estado, TipoActivo, SistemaOperativo, VersionSistemaOperativo, Ofimatica, VersionOfimatica, InformacionSoftware, Antivirus, Navegador, HerramientaCloud,InformacionHardware

admin.site.register(Activo)
admin.site.register(Estado)
admin.site.register(TipoActivo)
admin.site.register(SistemaOperativo)
admin.site.register(VersionSistemaOperativo)
admin.site.register(Ofimatica)
admin.site.register(VersionOfimatica)
admin.site.register(InformacionSoftware)
admin.site.register(Antivirus)
admin.site.register(Navegador)
admin.site.register (HerramientaCloud)
admin.site.register (InformacionHardware)
