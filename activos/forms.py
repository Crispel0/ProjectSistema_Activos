from django.urls import reverse_lazy
from .models import Activo, TipoActivo, Estado, InformacionSoftware, SistemaOperativo,VersionSistemaOperativo,Ofimatica, VersionOfimatica,Antivirus, Navegador,HerramientaCloud, InformacionHardware
from django.forms import ModelForm
from django import forms


class TipoActivoForm(ModelForm):
    class Meta:
        model = TipoActivo
        exclude=['usuario_registra', 'estado_software','estado_hardware']
    activo = forms.ModelChoiceField(queryset = Activo.objects.all())
    estado = forms.ModelChoiceField(queryset=Estado.objects.all())


class InformacionSoftwareForm(forms.ModelForm):
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
        exclude= ['sistema_operativo','version_sitema_op','id_activo','usuario_registro']

    

        
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        field_classes = {
        'tarjeta_madre_marca':'tarjeta_madre','tarjeta_madre_modelo':'tarjeta_madre','tarjeta_madre_serie':'tarjeta_madre',
        'fuente_poder_marca':'fuente_poder','fuente_poder_modelo':'fuente_poder','fuente_poder_serie':'fuente_poder','fuente_poder_capacidad':'fuente_poder',
        'procesador_marca':'procesador','procesador_modelo':'procesador','procesador_serie':'procesador',
        'disco_duro_1_marca': 'disco_duro_1','disco_duro_1_modelo':'disco_duro_1','disco_duro_1_serie':'disco_duro_1','disco_duro_1_capacidad':'disco_duro_1',
        'disco_duro_2_marca':'disco_duro_2','disco_duro_2_modelo':'disco_duro_2','disco_duro_2_serie':'disco_duro_2','disco_duro_2_capacidad':'disco_duro_2',
        'ram_slot_1_marca':'ram_slot_1','ram_slot_1_modelo':'ram_slot_1','ram_slot_1_serie':'ram_slot_1','ram_slot_1_capacidad':'ram_slot_1',
        'ram_slot_2_marca':'ram_slot_2','ram_slot_2_modelo':'ram_slot_2','ram_slot_2_serie':'ram_slot_2','ram_slot_2_capacidad':'ram_slot_2',
        'tarjeta_video_marca':'tarjeta_video','tarjeta_video_modelo':'tarjeta_video','tarjeta_video_serie':'tarjeta_video', 'tarjeta_video_capacidad':'tarjeta_video',
        'monitor_marca':'monitor','monitor_modelo':'monitor', 'monitor_serie':'monitor',
        'mouse_marca':'mouse','mouse_modelo':'mouse','mouse_serie':'mouse',
        'teclado_marca':'teclado','teclado_modelo':'teclado', 'teclado_serie':'teclado'


    }
        for field_name, field in self.fields.items():
            if field_name in field_classes:
                class_name = field_classes[field_name]
                classes = {
                    'class': class_name
                }
                field.widget.attrs.update(classes)
  
    
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
        exclude=['estado']


        
class VersionOfimaticaForm(ModelForm):
    class Meta:
        model = VersionOfimatica
        fields = '__all__'
        exclude=['estado']
