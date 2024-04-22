from django.db import models
from django.contrib.auth.models import User
from kvak.custom_enums import TileType, BackgroundType


class Žába(models.Model):
    isQueen = models.BooleanField(default=False)
    tileId = models.IntegerField()

class Player(models.Model):
    zaby = models.ManyToManyField(Žába)

class Game(models.Model):
    firstOnMove = models.BooleanField(default=True)
    moveCount = models.IntegerField(default=0)
    boardId = models.IntegerField()

    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1_reverse")
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2_reverse")

    isOver = models.BooleanField(default=False)

class Tile(models.Model):
    isFliped = models.BooleanField(default=False)
    type = models.IntegerField(choices=[(e.value, e.name) for e in TileType])
    backgroundType = models.IntegerField(choices=[(e.value, e.name) for e in BackgroundType])
    number = models.IntegerField(null=False)





class Board(models.Model):
    tiles = models.ManyToManyField(Tile)



class StouplNaSamce(models.Model):
    playerId = models.IntegerField()
    gameId = models.IntegerField()
    color = models.IntegerField()