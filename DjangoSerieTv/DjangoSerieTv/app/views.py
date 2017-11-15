"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Serie
from app.forms import QueryForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    series = Serie.getSeries()
    return render(request,
        'app/index.html',
        {
            'title':'Serie tv',
            'series':series
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
        
    context = {

        "title":"Crear Nueva Serie",
        "form": form,

    }

    return render(request, "app/serieForm.html", context)