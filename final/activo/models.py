from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Activo(models.Model):
    nombre = models.CharField(max_length=150)
    
    def __str__(self):
        return self.nombre
    
class Estado(models.Model):
    estado = models.CharField(max_length=150, verbose_name="Estado")
    
    def __str__(self):
        return self.estado

class TipoActivo(models.Model):
    marca = models.CharField(max_length=50, verbose_name="Marca")
    serie = models.CharField(max_length=50, verbose_name="Número de serie")
    activo = models.ForeignKey(Activo, on_delete=models.CASCADE, verbose_name="Activo")
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, verbose_name="Estado")
    estado_software = models.BooleanField(default=False)
    estado_hardware = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.serie
    
class SistemaOperativo(models.Model):
    nombre_sistema = models.CharField (max_length=150,unique=True, verbose_name="nombre del sistema")
    estado = models.BooleanField (default=True, verbose_name="Estado")
    def __str__(self):
        return self.nombre_sistema
    
class VersionSistemaOperativo (models.Model):
    version_sistema = models.CharField (max_length= 150, unique=True, verbose_name = "Version del sistema")
    sistema_operativo = models.ForeignKey(SistemaOperativo, on_delete=models.CASCADE)
    estado = models.BooleanField (default=True, verbose_name="Estado")

    
    def __str__(self)->str:
        return "%s | %s" %(self.sistema_operativo, self.version_sistema )
    
class Ofimatica (models.Model):
    paquete_ofimatica  = models.CharField (max_length=150,unique=True, verbose_name="Paquete de ofimatica")

    def __str__(self):
       return self.paquete_ofimatica

class VersionOfimatica(models.Model):
    version = models.CharField (max_length= 150, unique=True, verbose_name = "Version del paquete ofimatica")
    paquete = models.ForeignKey(Ofimatica, on_delete=models.CASCADE)
    
    def __str__(self):
        return "%s - %s" %(self.paquete, self.version)
    
class Antivirus(models.Model):
    antivirus = models.CharField(max_length=150, unique=True, verbose_name = "Versión de antivirus")
    
    def __str__(self):
        return self.antivirus
    
class Navegador(models.Model):
    navegador = models.CharField(max_length=150, unique=True, verbose_name = "Navegador web")
    
    def __str__(self):
        return self.navegador
    
class HerramientaCloud (models.Model):
    herramienta = models.CharField(max_length=150, unique=True, verbose_name="Herramienta cloud")    
    
    def __str__(self):
        return self.herramienta
        

class InformacionSoftware(models.Model): 
        
    sistema_operativo = models.ForeignKey(SistemaOperativo, on_delete=models.CASCADE)
    version_sistema_op= models.ForeignKey(VersionSistemaOperativo, on_delete=models.CASCADE, verbose_name="Versión de sistema operativo")
    ofimatica= models.ForeignKey(Ofimatica, on_delete=models.CASCADE)        
    version_ofimatica = models.ForeignKey(VersionOfimatica, on_delete=models.CASCADE)
    antivirus = models.ForeignKey(Antivirus, on_delete = models.CASCADE, null=True, blank=True) #Eliminar propiedades null y blank
    navegador_1 = models.ForeignKey(Navegador, on_delete = models.CASCADE, null=True, blank=True, related_name="navegador_1") #Eliminar propiedades null y blank
    navegador_2 = models.ForeignKey(Navegador, on_delete = models.CASCADE, null=True, blank=True, related_name="navegador_2") #Eliminar propiedades null y blank
    herramienta_cloud = models.ForeignKey (HerramientaCloud, on_delete = models.CASCADE, null=True, blank=True )#Eliminar propiedades null y blank
    id_activo = models.OneToOneField("TipoActivo", verbose_name="Activo", on_delete=models.CASCADE, null=True, blank = True) #Eliminar propiedades null y blank
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.id_activo
    

    
class InformacionHardware(models.Model):
    tarjeta_madre_marca = models.CharField(max_length=150, verbose_name= "Marca de motherboard")  
    tarjeta_madre_modelo = models.CharField(max_length=150, verbose_name= "Modelo de motherboard")  
    tarjeta_madre_serie =  models.CharField(max_length=150, verbose_name= "Numero de serie de motherboard")  
    tarjeta_madre_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  
    fuente_poder_marca = models.CharField(max_length=150, verbose_name= "Marca de fuente")  
    fuente_poder_modelo = models.CharField(max_length=150, verbose_name= "Modelo de fuente")  
    fuente_poder_serie =  models.CharField(max_length=150, verbose_name= "Numero de serie de fuente")  
    fuente_poder_capacidad =  models.CharField(max_length=150, verbose_name= "capacidad de fuente")  
    fuente_poder_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  
    procesador_marca = models.CharField(max_length=150, verbose_name= "Marca de procesador")  
    procesador_modelo = models.CharField(max_length=150, verbose_name= "Modelo de procesador")  
    procesador_serie =  models.CharField(max_length=150, verbose_name= "Numero de procesador")  
    procesador_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  
    disco_duro_1_marca = models.CharField(max_length=150, verbose_name= "Marca de disco duro 1")  
    disco_duro_1_modelo = models.CharField(max_length=150, verbose_name= "Modelo de disco duro 1")  
    disco_duro_1_serie =  models.CharField(max_length=150, verbose_name= "Numero de disco duro 1")  
    disco_duro_1_capacidad =  models.CharField(max_length=150, verbose_name= "capacidad de disco duro 1")
    disco_duro_1_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  
    disco_duro_2_marca = models.CharField(max_length=150, verbose_name= "Marca de disco duro 2")  
    disco_duro_2_modelo = models.CharField(max_length=150, verbose_name= "Modelo de disco duro 2")  
    disco_duro_2_serie =  models.CharField(max_length=150, verbose_name= "Numero de disco duro 2")  
    disco_duro_2_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  
    disco_duro_2_capacidad =  models.CharField(max_length=150, verbose_name= "capacidad de disco duro 2")
    ram_slot_1_marca = models.CharField(max_length=150, verbose_name= "Marca de memoria ram 1")  
    ram_slot_1_modelo = models.CharField(max_length=150, verbose_name= "Modelo de memoria ram 1")  
    ram_slot_1_serie =  models.CharField(max_length=150, verbose_name= "Numero de memoria ram 1")  
    ram_slot_1_capacidad =  models.CharField(max_length=150, verbose_name= "capacidad de memoria ram 1")
    ram_slot_1_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    ram_slot_2_marca = models.CharField(max_length=150, verbose_name= "Marca de memoria ram 2")  
    ram_slot_2_modelo = models.CharField(max_length=150, verbose_name= "Modelo de memoria ram 2")  
    ram_slot_2_serie =  models.CharField(max_length=150, verbose_name= "Numero de memoria ram 2")  
    ram_slot_2_capacidad =  models.CharField(max_length=150, verbose_name= "capacidad de memoria ram 2")
    ram_slot_2_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    tarjeta_video_marca = models.CharField(max_length=150, verbose_name= "Marca de tarjeta de video")  
    tarjeta_video_modelo = models.CharField(max_length=150, verbose_name= "Modelo de tarjeta de video")  
    tarjeta_video_serie =  models.CharField(max_length=150, verbose_name= "Numero de tarjeta de video")  
    tarjeta_video_capacidad =  models.CharField(max_length=150, verbose_name= "Capacidad tarjeta de video")  
    tarjeta_video_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    monitor_marca = models.CharField(max_length=150, verbose_name= "Marca de monitor")  
    monitor_modelo = models.CharField(max_length=150, verbose_name= "Modelo de monitor")  
    monitor_serie =  models.CharField(max_length=150, verbose_name= "Numero de monitor")  
    monitor_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    mouse_marca = models.CharField(max_length=150, verbose_name= "Marca de mouse")  
    mouse_modelo = models.CharField(max_length=150, verbose_name= "Modelo de mouse")  
    mouse_serie =  models.CharField(max_length=150, verbose_name= "Serie de mouse")  
    mouse_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    teclado_marca = models.CharField(max_length=150, verbose_name= "Marca de teclado")  
    teclado_modelo = models.CharField(max_length=150, verbose_name= "Modelo de teclado")  
    teclado_serie =  models.CharField(max_length=150, verbose_name= "Serie de teclado")  
    teclado_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica") 
    user = models.ForeignKey(User, on_delete= models.CASCADE, null=True, blank=True)
    id_activo = models.OneToOneField("TipoActivo", verbose_name="Activo", on_delete=models.CASCADE, null=True, blank = True) #Eliminar propiedades null y blank
