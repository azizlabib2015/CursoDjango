"""
Definition of models.
"""

from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=20)
    year = models.IntegerField()
    GENRES = ((0,"Action"),(1,"Adventure"),(2,"Strategy"),(3,"RPG"),(4,"Sport"))
    genre = models.IntegerField(choices=GENRES)
    PLATFORMS = ((0,"PC"),(1,"PS4"),(2,"XBOXONE"))
    platform = models.IntegerField(choices=PLATFORMS)
    score = models.IntegerField()
    online=models.BooleanField()
    pegi=models.IntegerField()

    #devolver todas las series
    def getGames():
        games = Game.objects.all()
        return games

    def getGame(clave):
        try:
            game = Game.objects.get(pk=clave)
        except Game.DoesNotExist:
            game = None

        return game

    def getGamesByFilter():
        games = Game.objects.values_list("id","name","score").order_by("score").reverse()
        return games
    def getGameSearch(data):
        
        try:
            games = Game.objects.filter(name__icontains=data)|Game.objects.filter(publisher__icontains=data)
        except Game.DoesNotExist:
            games = None
        return games

    