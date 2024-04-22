from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    id = 3232321
    return HttpResponseRedirect(reverse("game", kwargs={"code":id}))

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