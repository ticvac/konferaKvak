from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template.response import TemplateResponse
from django.views.generic import TemplateView


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    id = 3232321
    return HttpResponseRedirect(reverse("play", kwargs={"code":id}))

class PlayView(TemplateView):
    template_name = "kvak/game.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        code = self.kwargs.get("code")

        for i in range(8):
            context_data["tiles"].append([])
            for j in range(8):
                context_data["tiles"][-1].append("T")

        return context_data