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
        context_data = super().get_context_data(**kwargs)
        code = self.kwargs.get("code")

        context_data["tiles"] = []
        for i in range(8):
            context_data["tiles"].append([])
            for j in range(8):
                context_data["tiles"][-1].append("T")

        return context_data

def play_move(reques):
    tile1 = 0
    tile2 = 2
    is_queen = False