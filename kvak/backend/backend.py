
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
    print(frog1.stunned)
    #the gave, we are evaluating
    
    #player whos move it is
    player = get_player_from_game(game)
    #frogs of the playing player
    frogs = list(player.zaby.all())

    if check_valid_move(start,destiny, frogs, frog1, frog2):
        if destiny.type!=7:#klada
            kill_frog_on_tile(destiny)
        else:
            kill_frog_klada(destiny,frog1,frog2)
        move(destiny,frog1)
        
        evaluate_destiny(destiny,frog1,game,player,frogs)
        decrease_stunned(frogs)
        if destiny.type not in [1,2]: #leknin a komar
            game.moveCount += 1
        game.save()



def kill_frog_klada(tile,frog1,frog2):
    frogs_on_klada = Žába.objects.filter(tile=tile)
    if len(frogs_on_klada) == 0:
        return True
    if len(frogs_on_klada)==1:
        if frogs_on_klada[0].isQueen:
            frogs_on_klada[0].delete()

        if frog1.isQueen:
            for frog in frogs_on_klada:
                frog.delete()
    if len(frogs_on_klada) == 2:
        if frog1.isQueen:
            for frog in frogs_on_klada:
                frog.delete()
        else:
            if frog1.player != frog2.player:
                frog2.delete()





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

    if turn_count % 2 == 0:
        return game.player1
    else:
        return game.player2

def get_frog_from_id(id)->Žába:
    try:
        return Žába.objects.get(id=id)
    except:
        #print("nemůžu najít žábu")
        return None



def kill_frog_on_tile(tile):
    try:
        frogs_to_kill = Žába.objects.filter(tile=tile)
        for frog in frogs_to_kill:
            frog.delete()
    except:
        pass

def move(tile,frog):
    frog.tile = tile
    tile.isFliped = True
    tile.save()
    frog.save()

def evaluate_destiny(tile:Tile,frog:Žába,game:Game,player:Player,frogs:list[Žába]):
    if tile.type == 1:#leknin
        on_leknin(frog,frogs)
    if tile.type == 2:#komar
        on_komar(frog, game)
    if tile.type == 3:#bahno
        on_bahno(frog)
    if tile.type == 4:#stika
        on_stika(tile)
    if tile.type == 5:#rakos
        return True
    if tile.type == 7:
        on_klada(tile)
    if tile.type in [60,61,62,63,64,65]: #mozna samci maji *
        on_samec(player,game,tile,frog)

def on_leknin(frog,frogs):
    for zaba in frogs:
        if zaba==frog:
            continue
        zaba.stunned =2
        zaba.save()

def on_komar(frog, game):
    game.komar_frog = frog.id
    frog.stunned=1
    frog.save()

def on_bahno(frog):
    frog.stunned=1
    frog.save()
    return

def on_stika(tile):
    kill_frog_on_tile(tile)

def on_klada(tile:Tile)->bool:
    #povolit jen když tam je max jedna žába
    try:
        frogs = Žába.objects.filter(tile=tile)
        if len(frogs)>1:
            return False
        if len(frogs) == 1:
            if frogs[0].isQueen == True:
                return False
            else:
                return True
    except:
        return True


def on_samec(player:Player,game:Game,tile:Tile,frog:Žába):
    if frog.isQueen:
        try:
            StouplNaSamce.objects.get(playerId=player.id,gameId=game.id,color=tile.type)
            print("balls")
            return False
        except:
            zaba = Žába.objects.create(isQueen=False, tile=tile, player=player)
            zaba.save()
            # TODO create stoupl na samce
            sns = StouplNaSamce.objects.create(
                playerId = player.id,
                gameId = game.id,
                color = tile.type,
            )
            sns.save()
    return
        


def check_valid_move(start:Tile,destiny:Tile,frogs:list[Žába],frog1:Žába,frog2:Žába):
    if start==destiny:
        print("nemůžeš z jednoho políčka na to samé")
        return False
    
    if frog1.stunned>0:
        print("jsi v bahně co děláš")
        return False
    
    if frog1 not in frogs:
        print("není tvůj tah kámo")
        return False
    
    if not adjecent(start,destiny):
        return False
    
    if teammate_frog(frogs,frog1,frog2,destiny):
        return False
    
    if queen_given_birth(frogs, frog1):
        return False
    
    return True

def adjecent(tile1,tile2):
    num1 = tile1.number
    num2 = tile2.number

    if abs(num1-num2) in [1,8]:
        return True
    else: 
        return False

def teammate_frog(frogs:list[Žába],frog1,frog2:Žába,tile:Tile):
    if tile.type == 7:
        if frog1.isQueen:
            for frog in frogs:
                if frog.tile == tile:
                    return True
            return False
        else: 
            frogs_on_klada = Žába.objects.filter(tile=tile)
            if len(frogs_on_klada)==1:
                if frog1.player==frogs_on_klada[0].player and frogs_on_klada[0].isQueen:
                    return True
                return False
            if len(frogs_on_klada)==2:
                if frog1.player==frog2.player:
                    return True
                return False

    elif frog2 in frogs:
        return True
    else: 
        return False

def queen_given_birth(frogs, frog1):
    for frog in frogs:
        for zaba in frogs:
            if frog.tile == zaba.tile and zaba != frog:
                if frog.isQueen or zaba.isQueen:
                    if frog == frog1 or zaba == frog1:
                        return False
                    else:
                        return True
    return False

def decrease_stunned(frogs):
    for frog in frogs:
        if frog.stunned >0:
            frog.stunned -= 1
            frog.save()