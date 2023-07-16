from .models import Activo, TipoActivo, Estado, InformacionSoftware, SistemaOperativo,VersionSistemaOperativo,Ofimatica, VersionOfimatica,Antivirus, Navegador,HerramientaCloud, InformacionHardware
from django.forms import ModelForm
from django import forms


class TipoActivoForm(ModelForm):
    class Meta:
        model = TipoActivo
        exclude=['usuario_registra', 'estado_software','estado_hardware']
    activo = forms.ModelChoiceField(queryset = Activo.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())


class InformacionSoftwareForm(ModelForm):
    class Meta:
        model = InformacionSoftware
        exclude=['id_activo', 'registrado', 'usuario_registro']
    sistema_operativo = forms.ModelChoiceField(queryset = SistemaOperativo.objects.filter(estado=True))
    version_sistema_op = forms.ModelChoiceField(queryset = VersionSistemaOperativo.objects.all())
    ofimatica = forms.ModelChoiceField(queryset= Ofimatica.objects.all())
    version_ofimatica = forms.ModelChoiceField(queryset= VersionOfimatica.objects.all())
    antivirus = forms.ModelChoiceField(queryset = Antivirus.objects.all())
    navegador_1 = forms.ModelChoiceField(queryset = Navegador.objects.all()) 
    navegador_2 = forms.ModelChoiceField(queryset = Navegador.objects.all())
    herramienta_cloud = forms.ModelChoiceField(queryset = HerramientaCloud.objects.all()) 

class InformacionHardwareForm(ModelForm):
    class Meta:
        model = InformacionHardware
        fields = '__all__'
  
    
class SistemaOperativoForm(ModelForm):
    class Meta:
        model = SistemaOperativo
        exclude=['estado']


class VersionSistemaOperativoForm(ModelForm):
    class Meta:
        model = VersionSistemaOperativo
        exclude=['estado']
        
    sistema_operativo = forms.ModelChoiceField(queryset = SistemaOperativo.objects.filter(estado=True))


class OfimaticaForm(ModelForm):
    class Meta:
        model = Ofimatica
        fields = '__all__'


        
class VersionOfimaticaForm(ModelForm):
    class Meta:
        model = VersionOfimatica
        fields = '__all__'