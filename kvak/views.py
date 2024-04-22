from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from .models import Game, Board, Tile, Player, Žába
from .custom_enums import TileType, BackgroundType

import random


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    game = Game.objects.create()
    board = Board.objects.create()
    board.save()
    game.board = board

    tile_ids = list(range(64))
    random.shuffle(tile_ids)

    for i in range(6):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )
    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )    
    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )

    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )

    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.BAHNO,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )

    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.STIKA,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.STIKA,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )

    for i in range(10):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )
    for i in range(3):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )
    for i in range(3):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )
    
    for i in [TileType.MODRY_SAMEC, TileType.ZLUTY_SAMEC, TileType.RUZOVY_SAMEC, TileType.ZELENY_SAMEC, TileType.CERVENY_SAMEC,FIALOVY_SAMEC]:
    
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.i,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )
    for i in [TileType.MODRY_SAMEC, TileType.ZLUTY_SAMEC, TileType.RUZOVY_SAMEC]:
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.i,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )
    for i in [TileType.ZELENY_SAMEC, TileType.CERVENY_SAMEC, TileType.FIALOVY_SAMEC]:
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.i,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )

    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA,
            backgroundType = BackgroundType.BEZ_STIKY,
            board = board
        )
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA,
            backgroundType = BackgroundType.STIKA_DOLE,
            board = board
        )
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA,
            backgroundType = BackgroundType.STIKA_NAHORE,
            board = board
        )
    
    #tile1 = game.tiles.get(number=1)
    player1 = Player.objects.create()
    zaba = Žába.objects.create(
        isQueen = True,
        tile = game.tiles.get(number=0),
        player = player1
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.tiles.get(number=1),
        player= player1
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.tiles.get(number=8),
        player= player1
    )
    player1.save()
    player2 = Player.objects.create()
    zaba = Žába.objects.create(
        isQueen = True,
        tile = game.tiles.get(number=63),
        player = player2
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.tiles.get(number=62),
        player= player2
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.tiles.get(number=55),
        player= player2
    )

    game.save()
    id = game.id
    return HttpResponseRedirect(reverse("game", kwargs={"code":id}))

def game(request, code):
    args = {}
    args["tiles"] = []
    for i in range(8):
        args["tiles"].append([])
        for j in range(8):
            args["tiles"][-1].append("T")
    return TemplateResponse(request, "kvak/game.html", args) 