
from ..models import Tile,Player,Game,Žába,Board,StouplNaSamce

def next_state(tile1Num:int,tile2Num:int,gameid:int,frog1:int,frog2:int):
    game = get_game_from_id(gameid)
    #tile from which we are moving
    start = get_tile_from_id(tile1Num, game)
    #tile where we move
    destiny = get_tile_from_id(tile2Num, game)

    #moving frog
    frog1 = get_frog_from_id(frog1)
    #frog to kill if -1 then nothing
    frog2 = get_frog_from_id(frog2)

    #the gave, we are evaluating
    
    #player whos move it is
    player = get_player_from_game(game)
    #frogs of the playing player
    frogs = list(player.zaby.all())

    if check_valid_move(start,destiny, frogs, frog1, frog2):
        kill_frog_on_tile(destiny)
        move(destiny,frog1)
        evaluate_destiny(destiny,frog1,game,player)
        game.moveCount += 1
        game.save()




def get_tile_from_id(tileNum, game):
    try:
        return game.board.tiles.get(number=tileNum)
        # return Tile.objects.get(, number=tileNum)
    except:
        print("nemůžu najít tile")
        return "koule"

def get_game_from_id(gameid):
    try:
        return Game.objects.get(id=gameid) 
    except:
        print("nemůžu najít hru")
        return "koule"

def get_player_from_game(game):
    turn_count = game.moveCount

    if turn_count % 2==0:
        return game.player1
    else:
        return game.player2

def get_frog_from_id(id)->Žába:
    print(id)
    try:
        return Žába.objects.get(id=id)
    except:
        print("nemůžu najít žábu")
        return None

def kill_frog_on_tile(tile):
    try:
        frog_to_kill = Žába.objects.get(tile_id=tile.id)
        frog_to_kill.delete()
    except:
        pass

def move(tile,frog):
    frog.tile = tile
    frog.save()

def evaluate_destiny(tile:Tile,frog:Žába,game:Game,player:Player):
    if tile.type == 1:
        on_leknin(frog)
    if tile.type == 2:
        on_komar(frog)
    if tile.type == 3:
        on_bahno(frog)
    if tile.type == 4:
        on_stika(frog)
    if tile.type == 5:
        return True
    if tile.type == 6:#mozna klada ma sedm
        on_klada(tile)
    if tile.type in [61,62,63,64,65]: #mozna samci maji 7*
        on_samec(player,game,tile,frog)

def on_leknin(frog):
    #nepřičti kolo
    #znovu dej hráči tah a forci ho pohnout se stejnou žábou jako předtím. (ostatním žábám dej can_move=Fals  možná)
    ...

def on_komar(frog):
    #nepřičti kolo
    #dej hráči tah, ale žába, kterou se předtím pohnul má can_move=False
    ...

def on_bahno(frog):
    frog.can_move=False
    frog.save()
    return

def on_stika(tile):
    kill_frog_on_tile(tile)

def on_klada(tile:Tile)->bool:
    #povolit jen když tam je max jedna žába
    try:
        frogs = Žába.objects.get(tileId=tile.id)
        if len(frogs)>1:
            return False
    except:
        return True

    #nepovolit když tam je královna
    try:
        Žába.objects.get(isQueen=True,tileId=tile.id)
        return False
    except:
        pass


def on_samec(player:Player,game:Game,tile:Tile,frog:Žába):
    if frog.isQueen:
        try:
            StouplNaSamce.objects.get(playerId=player.id,gameId=game.id,color=tile.type)
            return False
        except:
            Žába.objects.create(isQueen=False,tileId=tile.id)
            Žába.save()
    return
        


def check_valid_move(start:Tile,destiny:Tile,frogs:list[Žába],frog1:Žába,frog2:Žába):
    if start==destiny:
        return False
    
    if not frog1.can_move:
        return False
    
    if frog1 not in frogs:
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