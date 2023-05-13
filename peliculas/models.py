from django.db import models

# Create your models here.
class Peliculas(models.Model):
    fecha_ingreso = models.DateField(auto_now_add=True)
    titulo = models.CharField(max_length=1028)
    version = models.CharField(max_length=1028)
    cpl = models.CharField(blank = True, max_length=1028)
    
    def __str__(self):
        return f"{self.fecha_ingreso} \n Película: {self.titulo} \n versión {self.version} \n CPL: {self.cpl} "
    
    
class Kdm(models.Model):
    fecha_ingreso_kdm = models.DateField(auto_now_add=True)
    titulo_kdm = models.CharField(max_length=1028)
    cpl_kdm = models.CharField(max_length=1028)
    servidor_kdm = models.IntegerField()
    fecha_apertura = models.DateTimeField(null=True, blank=True)
    fecha_clausura= models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.fecha_ingreso_kdm} \nKDM: {self.titulo_kdm} \n  CPL: {self.cpl_kdm} \n Servidor: {self.servidor_kdm} \n Apertura = {self.fecha_apertura} \n Cierra: {self.fecha_clausura}" 

class Sesion(models.Model): 
    fecha_ingreso_ss = models.DateField(auto_now_add=True)
    datetime_sesion = models.DateField()
    titulo_sesion = models.CharField(max_length=1028)
    version_sesion = models.CharField(blank = True, max_length=1028)
    SALA_CHOICES = (
        ("K1", "Kursaal 1"),
        ("K2", "Kursaal 2"),
        ("TVE", "Teatro Victoria Eugenia"),
    )
    sala = models.CharField(max_length=1028, choices=SALA_CHOICES)
