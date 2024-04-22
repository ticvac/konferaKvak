from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    id = 3232321
    return HttpResponseRedirect(reverse("game", kwargs={"code":id}))

def game(request, code):
    args = {}
    args["tiles"] = []
    args["game_id"] = code
    args["premoved_frog"] = 233
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
    return TemplateResponse(request, "kvak/game.html", args) 

def play_move(request, code):
    tile1_id = -1
    tile2_id = -1
    if request.method == "POST":
        tile1_id = int(request.POST["tile_id_1"])
        tile2_id = int(request.POST["tile_id_2"])
    
    return HttpResponse(str(tile1_id) + " - " + str(tile2_id))