"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from app.models import Game
from app.forms import FormGame
from app.forms import FormFilter

def home(request):
    #form = FormFilter(request.POST or None)
    games=[]
    #if form.is_valid():
    #    instance=form.dataSearch
    #    
    if request.method == 'GET': # If the form is submitted

        instance = request.GET.get('dataSearch', None)
        if instance is not None:
            games = Game.getGameSearch(instance)
            if len(games)==1:
                return HttpResponseRedirect('/show/%s' % games[0].id)
            elif len(games)<1:
                error="This Games not exists"
                return render(request,
                'app/index.html',
                {
                    'title':'Game List',
                    'games':games,
                    'divError':True,
                    'error':error
                })
        else:
            games = Game.getGames()
        
    else:
        games = Game.getGames()
    return render(request,
        'app/index.html',
        {
            'title':'Game List',
            'games':games
        })


def show(request,id):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    game = Game.getGame(id)
    if game is None:
        games = Game.getGames()
        error="This Game(id="+id+") not exist"
        return render(request,
        'app/index.html',
        {
            'title':'Game List',
            'games':games,
            'divError':True,
            'error':error
        })

    else:
        return render(request,
        'app/show.html',
        {
            'title':'Information '+game.name,
            'game':game
        })
def create(request):
    form = FormGame(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.clean()
            return HttpResponseRedirect('/show/%s' % instance.id)
        else:
            error=""
            for e in form.errors:
                error+=e+"\n"
            return render(request, "app/formGame.html", {"title":"Create New Game","form": form,'divError':True,
            'error':error})
    
        
    context = {

        "title":"Create New Game",
        "form": form,

    }
    return render(request, "app/formGame.html", context)

def edit(request,id):
    game = Game.getGame(id)
    form = FormGame(request.POST or None,instance=game)
    if  request.method=='POST':
    
        if form.is_valid():
            instance2 = form.save(commit=False)
            instance2.save()
            return HttpResponseRedirect('/show/%s' % instance2.id)
        else:
            error=""
            for e in form.errors:
                error+=e+"\n"
            return render(request, "app/formGame.html", {"title":"Edit Game","form": form,'divError':True,
            'error':error})
    

    context = {
        "title":"Edit Game",
        "form": form
        }
    return render(request, "app/formGame.html", context)

def remove(request,id):
    Game.objects.filter(pk=id).delete()
    return HttpResponseRedirect('/')

def ranking(request):
    games = Game.getGamesByFilter()
    return render(request,
        'app/ranking.html',
        {
            'title':'Rankings og Games',
            'games':games
        })

def not_found(request):
    return render(request,'app/errors.html')