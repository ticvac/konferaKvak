from enum import Enum

class TileType(Enum):
    LEKNIN = 1
    KOMAR = 2
    BAHNO = 3
    STIKA = 4
    RAKOS = 5
    MODRY_SAMEC = 60
    FIALOVY_SAMEC = 61
    CERVENY_SAMEC = 62
    RUZOVY_SAMEC = 63
    ZELENY_SAMEC = 64
    ZLUTY_SAMEC = 65
    KLADA = 7

class BackgroundType(Enum):
    BEZ_STIKY = 1
    STIKA_DOLE = 2
    STIKA_NAHORE = 3
