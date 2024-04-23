from models import Tile,Player,Game,Žába,Board

def next_state(tile1Num:int,tile2Num:int,gameid:int):
    start = get_tile_from_id(tile1Num)
    destiny = get_tile_from_id(tile2Num)

    frog = get_frog_from_tile(start)

    game = get_game_from_id(gameid)

    player = get_player_from_game(game)

def get_frog_from_tile(tile):
    return Žába.objects.get(tile=tile)

def get_tile_from_id(tileNum):
    return Tile.objects.get(number=tileNum)

def get_game_from_id(gameid):
    return Game.objects.get(id=gameid) #game might not have id 

def get_player_from_game(game):
    turn_count = game.moveCount

    if turn_count%2==0:
        return game.player1
    else:
        return game.player2
