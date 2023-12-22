from django.db import models
from django.contrib.auth.models import User
from usuarios.models import  Usuario

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
    usuario_registra = models.ForeignKey(Usuario, on_delete= models.CASCADE)

    def __str__(self):
        return self.serie
  
class SistemaOperativo(models.Model):
    nombre_sistema = models.CharField (max_length=150,unique=True, verbose_name="nombre del sistema")
    estado = models.BooleanField (default=True, verbose_name="Estado")
    def __str__(self):
        return self.nombre_sistema
   
    
class VersionSistemaOperativo (models.Model):
    version_sistema = models.CharField (max_length= 150, unique=True)
    sistema_operativo = models.ForeignKey(SistemaOperativo, on_delete=models.CASCADE, verbose_name="version sistema operativo")
    estado = models.BooleanField (default=True, verbose_name="Estado")

  
    def __str__(self)->str:
        return  self.version_sistema

        
class Ofimatica (models.Model):
    paquete_ofimatica  = models.CharField (max_length=150,unique=True, verbose_name="Paquete de ofimatica")
    estado = models.BooleanField (default=True, verbose_name="Estado")

    def __str__(self):
       return self.paquete_ofimatica

class VersionOfimatica(models.Model):
    
    version = models.CharField (max_length= 150, unique=True, verbose_name = "Version del paquete ofimatica")
    paquete = models.ForeignKey(Ofimatica, on_delete=models.CASCADE)
    estado = models.BooleanField (default=True, verbose_name="Estado")

    
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
    antivirus = models.ForeignKey(Antivirus, on_delete = models.CASCADE , null=True) #Eliminar propiedades null y blank aceptan valores nulos o en blanco
    navegador_1 = models.ForeignKey(Navegador, on_delete = models.CASCADE,related_name="navegador_1", null=True) #Eliminar propiedades null y blank
    navegador_2 = models.ForeignKey(Navegador, on_delete = models.CASCADE,related_name="navegador_2", null=True) #Eliminar propiedades null y blank
    herramienta_cloud = models.ForeignKey (HerramientaCloud, on_delete = models.CASCADE, null=True) #Eliminar propiedades null y blank
    id_activo = models.OneToOneField("TipoActivo", verbose_name="Activo", on_delete=models.CASCADE, null=True) #Eliminar propiedades null y blank
    usuario_registro = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.id_activo
    

    
class InformacionHardware(models.Model):
    tarjeta_madre_marca = models.CharField(max_length=150,        verbose_name= "Marca motherboard")
    tarjeta_madre_modelo = models.CharField(max_length=150,       verbose_name= "Modelo motherboard")  
    tarjeta_madre_serie =  models.CharField(max_length=150,       verbose_name= "Serie de motherboard")
    tarjeta_madre_no_aplica =  models.BooleanField(default=False, verbose_name= "No aplica")  

    fuente_poder_marca = models.CharField(max_length=150, verbose_name="Marca fuente")  
    fuente_poder_modelo = models.CharField(max_length=150,verbose_name= "Modelo fuente")  
    fuente_poder_serie =  models.CharField(max_length=150,verbose_name= "Serie serie fuente")  
    fuente_poder_capacidad =  models.IntegerField(                verbose_name= "capacidad fuente")  
    fuente_poder_no_aplica =  models.BooleanField(default=False,  verbose_name= "No aplica") 

    procesador_marca = models.CharField(max_length=150,           verbose_name= "Marca procesador")  
    procesador_modelo = models.CharField(max_length=150,          verbose_name= "Modelo procesador")  
    procesador_serie =  models.CharField(max_length=150,          verbose_name= "Serie procesador")  
    procesador_no_aplica =  models.BooleanField(default=False,    verbose_name= "No aplica")

    disco_duro_1_marca = models.CharField(max_length=150,         verbose_name= "Marca disco duro 1")  
    disco_duro_1_modelo = models.CharField(max_length=150,        verbose_name= "Modelo disco duro 1")  
    disco_duro_1_serie =  models.CharField(max_length=150,        verbose_name= "Serie disco duro 1")  
    disco_duro_1_capacidad =  models.IntegerField(                verbose_name= "capacidad disco duro 1")
    disco_duro_1_no_aplica =  models.BooleanField(default=False,  verbose_name= "No aplica")  
    
    disco_duro_2_marca = models.CharField(max_length=150,         verbose_name= "Marca disco duro 2")
    disco_duro_2_modelo = models.CharField(max_length=150,        verbose_name= "Modelo disco duro 2")  
    disco_duro_2_serie =  models.CharField(max_length=150,        verbose_name= "Serie disco duro 2")
    disco_duro_2_capacidad =  models.IntegerField(                verbose_name= "capacidad disco duro 2")
    disco_duro_2_no_aplica =  models.BooleanField(default=False,  verbose_name= "No aplica")  

    ram_slot_1_marca = models.CharField(max_length=150,           verbose_name= "Marca memoria ram 1")  
    ram_slot_1_modelo = models.CharField(max_length=150,          verbose_name= "Modelo memoria ram 1")  
    ram_slot_1_serie =  models.CharField(max_length=150,          verbose_name= "Serie memoria ram 1")  
    ram_slot_1_capacidad =  models.IntegerField(                  verbose_name= "capacidad memoria ram 1")
    ram_slot_1_no_aplica =  models.BooleanField(default=False,    verbose_name= "No aplica")
    
    ram_slot_2_marca = models.CharField(max_length=150,           verbose_name= "Marca memoria ram 2")  
    ram_slot_2_modelo = models.CharField(max_length=150,          verbose_name= "Modelo memoria ram 2")  
    ram_slot_2_serie =  models.CharField(max_length=150,          verbose_name= "Serie memoria ram 2")  
    ram_slot_2_capacidad =  models.IntegerField(                  verbose_name= "capacidad memoria ram 2")
    ram_slot_2_no_aplica =  models.BooleanField(default=False,    verbose_name= "No aplica") 
    
    tarjeta_video_marca = models.CharField(max_length=150,        verbose_name= "Marca tarjeta video")
    tarjeta_video_modelo = models.CharField(max_length=150,       verbose_name= "Modelo tarjeta video")  
    tarjeta_video_serie =  models.CharField(max_length=150,       verbose_name= "Serie tarjeta video")  
    tarjeta_video_capacidad = models.IntegerField(                verbose_name= "Capacidad tarjeta video")  
    tarjeta_video_no_aplica = models.BooleanField(default=False,  verbose_name= "No aplica") 
    
    monitor_marca  = models.CharField(max_length=150,              verbose_name= "Marca monitor")  
    monitor_modelo = models.CharField(max_length=150,             verbose_name= "Modelo monitor")
    monitor_serie =  models.CharField(max_length=150,             verbose_name= "Serie monitor") 
    monitor_no_aplica = models.BooleanField(default=False,       verbose_name= "No aplica") 
    mouse_marca = models.CharField(max_length=150,                verbose_name= "Marca mouse")  
    mouse_modelo = models.CharField(max_length=150,               verbose_name= "Modelo mouse")  
    mouse_serie =  models.CharField(max_length=150,               verbose_name= "Serie mouse")  
    mouse_no_aplica = models.BooleanField(default=False,         verbose_name= "No aplica") 
    
    teclado_marca = models.CharField(max_length=150,              verbose_name= "Marca teclado")  
    teclado_modelo = models.CharField(max_length=150,             verbose_name= "Modelo teclado")  
    teclado_serie =  models.CharField(max_length=150,             verbose_name= "Serie teclado")  
    teclado_no_aplica = models.BooleanField(default=False,       verbose_name= "No aplica")
    
    usuario_registro = models.ForeignKey(Usuario, on_delete= models.CASCADE)
    id_activo = models.OneToOneField(TipoActivo, verbose_name="Activo", on_delete=models.CASCADE, null=True, blank = True)