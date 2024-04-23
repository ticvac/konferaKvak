from models import Tile,Player,Game,Žába,Board

def next_state(tile1Num:int,tile2Num:int,gameid:int):
    #tile from which we are moving
    start = get_tile_from_id(tile1Num)
    #tile where we move
    destiny = get_tile_from_id(tile2Num)
    #moving frog
    frog = get_frog_from_tile(start)
    #the gave, we are evaluating
    game = get_game_from_id(gameid)
    #player whos move it is
    player = get_player_from_game(game)
    #frogs of the playing player
    frogs = player.zaby

    if check_valid_move(start,destiny,frog,frogs):
        #kill_frog_on_tile(tile)
        #move(destiny,frog)




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


def check_valid_move(start,destiny,frog,frogs):
    if not adjecent(start,destiny):
        return False
    if occupied_by_teammate(destiny,frogs):
        return False
    if queen_given_birth(start,frogs):
        return False
    return True




def adjecent(tile1,tile2):
    num1 = tile1.number
    num2 = tile2.number

    if abs(num1-num2) in [1,8]:
        return True
    else: 
        return False

def occupied_by_teammate(tile,frogs):
    try:
        teammate = Žába.objects.get(tile = tile)
        if teammate in frogs:
            return True
    except: 
        return False

def queen_given_birth(tile,frogs):
    for frog in frogs:
        for zaba in frogs:
            if frog.tile == zaba.tile and zaba != frog and frog.tile == tile:
                if frog.isQueen or zaba.isQueen:
                    return True
    return False