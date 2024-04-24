from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from .models import Game, Board, Tile, Player, Žába
from .custom_enums import TileType, BackgroundType
from .backend.backend import *
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
    zaba.save()
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=1),
        player= player1
    )
    zaba.save()
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=8),
        player= player1
    )
    zaba.save()
    zaba = Žába.objects.create(
        isQueen = True,
        tile = game.board.tiles.get(number=63),
        player = player2
    )
    zaba.save()
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=62),
        player= player2
    )
    zaba.save()
    zaba = Žába.objects.create(
        isQueen = False,
        tile = game.board.tiles.get(number=55),
        player= player2
    )
    zaba.save()
    # for i in [0, 1, 8, 55, 63, 62]:
    #     tile = game.board.tiles.get(number=i)
    #     tile.isFliped = True
    #     tile.save()

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
        game = Game.objects.get(id=code)
        tiles = game.board.tiles.all().order_by("number")
        zaby1 = list(game.player1.zaby.all())
        zaby2 = list(game.player2.zaby.all())
        zaby = zaby1 + zaby2
        args["hrac_na_tahu"] = game.moveCount % 2 + 1
        args["komar_frog"] = game.komar_frog
        tiles_data = []
        for i in range(8):
            tiles_data.append([])
            for j in range(8):
                tile = tiles[i * 8 + j]
                tiles_data[-1].append(
                    {
                        "number" : i * 8 + j,
                        "image" : "tile_type_" + str(tile.type) + ".svg" if tile.isFliped else "bg_" + str(tile.backgroundType) + ".jpg",
                        "zaby" : [],
                    }
                )
                # zaby
                for zaba in zaby:
                    if zaba.tile.number == i * 8 + j:
                        tiles_data[-1][-1]["zaby"].append(
                            {
                                "id": zaba.id,
                                "image": "Frog_queen.png" if zaba.isQueen else "frog.png",
                                "color": "blue" if zaba in list(game.player1.zaby.all()) else "pink"
                            }
                        )
                
        args["tiles"] = tiles_data


        # for i in range(8):
        #     args["tiles"].append([])
        #     for j in range(8):
        #         args["tiles"][-1].append({
        #             "text" : "T",
        #             "zaby": [
        #                 {
        #                     "id" : i * 8 + j
        #                 },
        #                 # {
        #                 #     "id" : i * 8 + j + 63
        #                 # }
        #             ]
        #         })
        return args

def play_move(request, code):
    if request.method == "POST":
        tile1_id = int(request.POST["tile_id_1"])
        tile2_id = int(request.POST["tile_id_2"])
        zaba1_choice = int(request.POST["zaba_1_choice"])
        zaba2_choice = int(request.POST["zaba_2_choice"])
    next_state(tile1_id, tile2_id, code, zaba1_choice, zaba2_choice)
    
    return HttpResponseRedirect(reverse("game", kwargs={"code": code}))

    return HttpResponse(str(tile1_id) + " - " + str(tile2_id) + " |--!--| " + str(zaba1_choice) + " ! " + str(zaba2_choice))

def skip_komar(request, code, stunned_frog_id):
    if stunned_frog_id != -1:
        game = Game.objects.get(id=code)
        # game.moveCount += 1
        # game.save()
        zaba = Žába.objects.get(id=stunned_frog_id)
        if zaba.stunned > 0:
            zaba.stunned -= 1
        zaba.save()

    return HttpResponseRedirect(reverse("game", kwargs={"code": code}))

