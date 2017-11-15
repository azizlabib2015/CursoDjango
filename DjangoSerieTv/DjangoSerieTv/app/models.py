"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Serie(models.Model):
    titulo = models.CharField(max_length=20)
    productora = models.CharField(max_length=10)
    fecha = models.IntegerField()
    temporada = models.IntegerField()
    GENEROS = ((0,"Accion"),(1,"Historica"),(2,"Terror"),(3,"Drama"),(4,"Ficcion"),(5,"Policiaca"))
    genero = models.IntegerField(choices=GENEROS)
    ESTADO = ((0,"Produccion"),(1,"En Emision"),(2,"Finalizada"))
    estado=models.IntegerField(choices=ESTADO)

    #devolver todas las series
    def getSeries():
        series=Serie.objects.all()
        return series
    #devolver una serie
    def getSerie(clave):
        serie=Serie.objects.get(pk=clave)
        return serie
