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
    estado = models.IntegerField(choices=ESTADO)

    #devolver todas las series
    def getSeries():
        series = Serie.objects.all()
        return series
    #devolver una serie
    def getSerie(clave):
        serie = Serie.objects.get(pk=clave)
        return serie
    #devolver todas la lista del parametro de entrada
    def getListas(data):
        lista = []
        if data.lower() == "genero":
            series = Serie.objects.values_list(data,flat=True)
            for x in series:
                for k,v in Serie.GENEROS:
                    if k == x:
                        lista.append(v)
    
    
        else:
            lista = Serie.objects.values_list(data,flat=True).order_by(data)
        return lista

    def getSeriesByFilter(tipo,data):
        if tipo == "genero":
            for k,v in Serie.GENEROS:
                if v == data:
                    series = Serie.objects.values_list("id","titulo").filter(genero=k)
                    return series
        elif tipo=="fecha":
            series = Serie.objects.values_list("id","titulo").filter(fecha=data)
            return series
        elif tipo=="productora":
            series = Serie.objects.values_list("id","titulo").filter(productora=data)
            return series
        elif tipo=="todos":
            series = Serie.objects.filter(titulo__icontains=data)|Serie.objects.filter(productora__icontains=data)
            return series

class ModelFilter(models.Model):
    dataFilter = models.CharField(max_length=20

        