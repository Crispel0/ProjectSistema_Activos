from django.forms import ModelForm, widgets
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado','user']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Convertir la fecha almacenada en un objeto datetime.date
        if self.instance.fecha_nacimiento:
            self.initial['fecha_nacimiento'] = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')

