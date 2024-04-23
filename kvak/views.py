from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .models import Game, Board, Tile, Player, Žába
from .custom_enums import TileType, BackgroundType

import random


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    player1 = Player.objects.create()
    player1.save()
    player2 = Player.objects.create()
    player2.save()
    board = Board.objects.create()
    board.save()
    game = Game.objects.create(
        board = board,
        player1 = player1,
        player2 = player2,
    )


    tile_ids = list(range(64))
    random.shuffle(tile_ids)

    for i in range(6):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()
    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )  
        tile.save()  
    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.LEKNIN.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()

    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )
        tile.save()
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KOMAR.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()
    for i in range(4):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.BAHNO.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()

    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.STIKA.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )
        tile.save()
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.STIKA.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()

    for i in range(10):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()
    for i in range(3):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )
        tile.save()
    for i in range(3):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.RAKOS.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()
    
    for i in [TileType.MODRY_SAMEC, TileType.ZLUTY_SAMEC, TileType.RUZOVY_SAMEC, TileType.ZELENY_SAMEC, TileType.CERVENY_SAMEC, TileType.FIALOVY_SAMEC]:
    
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = i.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()
    for i in [TileType.MODRY_SAMEC, TileType.ZLUTY_SAMEC, TileType.RUZOVY_SAMEC]:
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = i.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )
        tile.save()
    for i in [TileType.ZELENY_SAMEC, TileType.CERVENY_SAMEC, TileType.FIALOVY_SAMEC]:
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = i.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()

    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA.value,
            backgroundType = BackgroundType.BEZ_STIKY.value,
            board = board
        )
        tile.save()
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA.value,
            backgroundType = BackgroundType.STIKA_DOLE.value,
            board = board
        )
        tile.save()
    for i in range(2):
        tile = Tile.objects.create(
            number = tile_ids.pop(),
            type = TileType.KLADA.value,
            backgroundType = BackgroundType.STIKA_NAHORE.value,
            board = board
        )
        tile.save()

    print(tile_ids)
    
    #tile1 = game.tiles.get(number=1)
    
    zaba = Žába.objects.create(
        isQueen = True,
        tile = game.board.tiles.get(number=0),
        player = player1
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=1),
        player= player1
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=8),
        player= player1
    )
    zaba = Žába.objects.create(
        isQueen = True,
        tile = game.board.tiles.get(number=63),
        player = player2
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=62),
        player= player2
    )
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=55),
        player= player2
    )

    game.save()
    id = game.id
    return HttpResponseRedirect(reverse("game", kwargs={"code": id}))

class GameView(TemplateView):
    template_name = "kvak/game.html"

    def get_context_data(self, **kwargs):
        args = super().get_context_data(**kwargs)
        code = self.kwargs.get("code")

        args = {}
        args["tiles"] = []
        args["game_id"] = code
        # args["premoved_frog"] = 9
        for i in range(8):
            args["tiles"].append([])
            for j in range(8):
                args["tiles"][-1].append({
                    "text" : "T",
                    "zaby": [
                        {
                            "id" : i * 8 + j
                        },
                        # {
                        #     "id" : i * 8 + j + 63
                        # }
                    ]
                })
        return args

def play_move(request, code):
    tile1_id = -1
    tile2_id = -1
    if request.method == "POST":
        tile1_id = int(request.POST["tile_id_1"])
        tile2_id = int(request.POST["tile_id_2"])
    
    return HttpResponse(str(tile1_id) + " - " + str(tile2_id))