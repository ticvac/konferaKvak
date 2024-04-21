from django.db import models
from django.contrib.auth.models import User
from enums import TileType,BackgroundType



class Game(models.Model):
    firstOnMove = models.BooleanField(default=True)
    moveCount = models.IntegerField(max=1000,default=1)
    boardId = models.IntegerField()

    player1 = models.ForeignKey(User, on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, on_delete=models.CASCADE)

    isOver = models.BooleanField(default=False)

class Tile(models.Model):
    isFliped = models.BooleanField(default=False)
    type = TileType()
    backgroundType = BackgroundType()
    number = models.IntegerField(null=False)


class Žába(models.Model):
    isQueen = models.BooleanField(default=False)
    tileId = models.IntegerField()



class Board(models.Model):
    tiles = models.ManyToManyField(Tile)


class Player(models.Model):
    zaby = models.ManyToManyField(Žába)

class StouplNaSamce(models.Model):
    playerId = models.IntegerField()
    gameId = models.IntegerField()
    color = models.IntegerField(max=5,min=0)