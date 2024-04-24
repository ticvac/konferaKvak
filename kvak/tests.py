from django.test import TestCase
from django.urls import reverse

from kvak.custom_enums import TileType
from kvak.models import Game


class GameInitTestCase(TestCase):
    """
        Tests if game initialization works correctly.
    """

    def setUp(self):
        self.client.get(reverse("init"))

        self.assertEqual(Game.objects.count(), 1)
        self.game = Game.objects.first()
        self.tiles = self.game.board.tiles.all()

    def test_tile_number(self):
        """ Tests if tiles are 1, 2, ..., 64 """
        # self.assertEqual(self.tiles.count(), 64)
        self.assertEqual([tile.number for tile in self.tiles.order_by("number")], list(range(64)))

    def test_number_of_types(self):
        """ Tests if number of tiles of each type is correct. """
        for type, num in [
            (TileType.LEKNIN, 14),
            (TileType.KOMAR, 8),
            (TileType.BAHNO, 4),
            (TileType.STIKA, 4),
            (TileType.RAKOS, 16),
            (TileType.KLADA, 6),
        ] + [(_type, 2) for _type in (
                TileType.MODRY_SAMEC,
                TileType.FIALOVY_SAMEC,
                TileType.CERVENY_SAMEC,
                TileType.RUZOVY_SAMEC,
                TileType.ZELENY_SAMEC,
                TileType.ZLUTY_SAMEC,
        )]:
            self.assertEqual(self.tiles.filter(type=type.value).count(), num)

    def zaba_test(self, hrac, places):
        """ Test if hrac's žábas starts in places """
        zaby = hrac.zaby.order_by("tile__number")
        self.assertEqual(zaby.count(), 3)
        self.assertEqual([zaba.tile.number for zaba in zaby], places)
        self.assertEqual([zaba.tile.board.game for zaba in zaby], [self.game]*3)

    def test_frogs(self):
        """ Tests starting positions of frogs """
        self.zaba_test(self.game.player1, [0, 1, 8])
        self.zaba_test(self.game.player2, [55, 62, 63])

