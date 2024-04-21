from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def init(request):
    # init game from database
    id = 3232321
    return HttpResponseRedirect(reverse("play", kwargs={"code":id}))

def play(request, code):
    return HttpResponse(str(code))