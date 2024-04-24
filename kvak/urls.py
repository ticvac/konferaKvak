from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("game/init", view=views.init, name="init"),
    path("game/<int:code>", view=views.GameView.as_view(), name="game"),
    path("game/<int:code>/play_move", view=views.play_move, name="play_move"),
    path("game/<int:code>/skip_komar/<int:stunned_frog_id>", view=views.skip_komar, name="skip_komar")
]