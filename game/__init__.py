import sys
import pygame as pg
from pygame import Surface
from .player import Player
from .tilemap import TileMap


class Game:
    def __init__(self):
        self.display_HEIGHT = 800
        self.display_WIDTH = 1200
        self.caption = "Jogo em Python"
        self.display = None
        self.time = pg.time.Clock()

        self.start()

    def start(self):
        self.display = pg.display.set_mode((self.display_WIDTH, self.display_HEIGHT))
        pg.display.set_caption(self.caption)

        self.player = Player()
        self.tile_map = TileMap()

        self.sprite_group = pg.sprite.Group()
        self.sprite_group.add(self.player)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    break

            keys = pg.key.get_pressed()
            self.player.move(keys)

            self.player.update()
            self.tile_map.update()

            self.display.fill("white")
            self.tile_map.draw(self.display)

            self.sprite_group.draw(self.display)

            pg.display.update()
            self.time.tick(60)
