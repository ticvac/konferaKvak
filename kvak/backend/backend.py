from models import Tile,Player,Game,Žába,Board

def next_state(tile1Num:int,tile2Num:int,gameid:int,frog1:int,frog2:int):
    #tile from which we are moving
    start = get_tile_from_id(tile1Num)
    #tile where we move
    destiny = get_tile_from_id(tile2Num)

    #moving frog
    frog1 = get_frog_from_id(frog1)
    #frog to kill if -1 then nothing
    frog2 = get_frog_from_id(frog2)

    #the gave, we are evaluating
    game = get_game_from_id(gameid)
    #player whos move it is
    player = get_player_from_game(game)
    #frogs of the playing player
    frogs = player.zaby

    if check_valid_move(start,destiny,frog1,frogs):
        move(destiny,frog1)




def get_tile_from_id(tileNum):
    return Tile.objects.get(number=tileNum)

def get_game_from_id(gameid):
    return Game.objects.get(id=gameid) 

def get_player_from_game(game):
    turn_count = game.moveCount

    if turn_count%2==0:
        return game.player1
    else:
        return game.player2

def get_frog_from_id(id)->Žába:
    try:
        return Žába.objects.get(id=id)
    except: return None

def kill_frog_on_tile(frog):
    #kills the frog
    pass

def move(tile,frog):
    frog.tile = tile
    frog.save()





def check_valid_move(start:Tile,destiny:Tile,frogs:list[Žába],frog1:Žába,frog2:Žába):
    if start==destiny:
        return False
    
    if frog1.can_move:
        return False
    
    if not adjecent(start,destiny):
        return False
    
    if teammate_frog(frogs,frog2,destiny):
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

def teammate_frog(frogs:list[Žába],frog:Žába,tile:Tile):
    if frog in frogs and tile.type!="KLADA":
        return True
    else: 
        return False

def queen_given_birth(tile,frogs):
    for frog in frogs:
        for zaba in frogs:
            if frog.tile == zaba.tile and zaba != frog and frog.tile == tile:
                if frog.isQueen or zaba.isQueen:
                    return True
    return False