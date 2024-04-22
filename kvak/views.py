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
    for i in range(8):
        args["tiles"].append([])
        for j in range(8):
            args["tiles"][-1].append("T")
    return TemplateResponse(request, "kvak/game.html", args) 

def play_move(reques):
    tile1 = 0
    tile2 = 2
    is_queen = False