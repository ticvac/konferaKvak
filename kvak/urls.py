from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("game/init", view=views.init, name="init"),
    path("game/<int:code>", view=views.play, name="game")

]