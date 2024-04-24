from django.db import models
from django.contrib.auth.models import User
from kvak.custom_enums import TileType, BackgroundType

class Board(models.Model):
    ...

class Tile(models.Model):
    isFliped = models.BooleanField(default=False)
    type = models.IntegerField(choices=[(e.value, e.name) for e in TileType])
    backgroundType = models.IntegerField(choices=[(e.value, e.name) for e in BackgroundType])
    number = models.IntegerField(null=False)
    board = models.ForeignKey(Board, related_name="tiles", null=False, on_delete=models.CASCADE)


class Player(models.Model):
    ...

class Žába(models.Model):
    isQueen = models.BooleanField(default=False)
    tile = models.ForeignKey(Tile, related_name = "zaby", null=False, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, related_name="zaby", null=False, on_delete=models.CASCADE)
    stunned = models.IntegerField(default=0)

class Game(models.Model):
    firstOnMove = models.BooleanField(default=True)
    moveCount = models.IntegerField(default=0)
    board = models.OneToOneField(Board, on_delete=models.CASCADE)

    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player1_reverse")
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player2_reverse")

    isOver = models.BooleanField(default=False)

    komar_frog = models.IntegerField(default=-1)


class StouplNaSamce(models.Model):
    playerId = models.IntegerField()
    gameId = models.IntegerField()
    color = models.IntegerField()