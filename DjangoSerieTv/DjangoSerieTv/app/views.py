"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Serie
from app.forms import QueryForm
from app.forms import FormFilter



def home(request):
    form = FormFilter(request.POST or None)
    series=[]
    errores=[]
    if form.is_valid():
        instance=form.instance.dataFilter
        series = Serie.getSeriesByFilter("todos",instance)
        
    else:
        series = Serie.getSeries()
    return render(request,
        'app/index.html',
        {
            'title':'Serie tv',
            'series':series,
            'form':form,
            'errores':errores
        })

def ver(request,id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    serie = Serie.getSerie(id)
    return render(request,
        'app/ver.html',
        {
            'title':'Informacion Serie',
            'serie':serie
        })

def crear(request):
    form = QueryForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/ver/%s' % instance.id)
        
    context = {

        "title":"Crear Nueva Serie",
        "form": form,

    }

    return render(request, "app/serieForm.html", context)



def editar(request,id):
    #comprobar si el parametro id es correcto
    if id=="":
        return render(request, "app/serieForm.html", context)
    
    serie = Serie.getSerie(id)
    form = QueryForm(request.POST or None,instance=serie)
    if form.is_valid():
        instance2 = form.save(commit=False)
        instance2.save()
        return HttpResponseRedirect('/ver/%s' % instance2.id)

    context = {
        "title":"Editar Serie",
        "form": form
        }
    return render(request, "app/serieForm.html", context)

def borrar(request,id):
    Serie.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/')

def listar(request,data):
    lista=Serie.getListas(data)
    lista2=set(lista)
    datas=data.capitalize()
    context = {
        "title":datas,
        "lista":lista2
        }
    return render(request, "app/listTemplate.html", context)

def verData(request,tipo,data):
    series=Serie.getSeriesByFilter(tipo.lower(),data)
    
    context = {
        "title":data,
        "series":series
        }
    return render(request, "app/verData.html", context)
    