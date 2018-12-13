from django.db import models

# Create your models here.
class Comunidad(models.Model):
    nombre=models.CharField(max_length=45)
    ubicacion=models.CharField(max_length=45)
    nombreCordinadores=models.CharField(max_length=45)
    nombresAgentesPastorales=models.CharField(max_length=45)
    nombresMisnistroComunion=models.CharField(max_length=45)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre=models.CharField(max_length=45)
    tipo=models.CharField(max_length=45)
    fecha=models.CharField(max_length=45)
    hora=models.CharField(max_length=45)
    comunidad = models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Solicitud(models.Model):
    sacramento=models.CharField(max_length=45)
    nombreP=models.CharField(max_length=45)
    apellidoP=models.CharField(max_length=45)
    nombreH=models.CharField(max_length=45)
    apellidoH=models.CharField(max_length=45)
  
    def __str__(self):
        return self.sacramento

class AgentesPatorales(models.Model):
    nombre=models.CharField(max_length=45)
    apellido=models.CharField(max_length=45)
    edad=models.CharField(max_length=45)
    tipoPersona=models.CharField(max_length=45)
    comu= models.ForeignKey(Comunidad,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.nombre

class Login(models.Model):
    usuario=models.CharField(max_length=45)
    password=models.CharField(max_length=45)
    comuLogin=models.ForeignKey(Comunidad,on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario

