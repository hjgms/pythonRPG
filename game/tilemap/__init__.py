import pygame as pg

class TileMap:
    def __init__(self):
        self.tile_width = 64
        self.tile_height = 64

        self.tilemap_image = pg.image.load("/Users/a./PycharmProjects/jogoEmPython/game/tilemap/Terrain/Ground/Tilemap_Flat.png").convert_alpha()

        self.map_layout = [
            [(1, 1), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(2, 1), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 2), (2, 3)],
            [(3, 1), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 2), (3, 3)]
        ]

        self.animated_tiles = {
            2: self.load_animated_tiles(2, 1, 2, 4)
        }

        self.current_frame = 0
        self.animation_speed = 0.1
        self.last_update = pg.time.get_ticks()

    def load_animated_tiles(self, start_row, start_col, end_row, end_col):
        frames = []
        for row in range(start_row - 1, end_row):
            for col in range(start_col - 1, end_col):
                x = col * self.tile_width
                y = row * self.tile_height
                frame = self.tilemap_image.subsurface(pg.Rect(x, y, self.tile_width, self.tile_height))
                frames.append(frame)
        return frames

    def update_animation(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 1000 * self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animated_tiles[2])

    def draw(self, display):
        for row_idx, row in enumerate(self.map_layout):
            for col_idx, (tile_row, tile_col) in enumerate(row):
                x = col_idx * self.tile_width
                y = row_idx * self.tile_height

                tile_x = (tile_col - 1) * self.tile_width
                tile_y = (tile_row - 1) * self.tile_height
                tile_image = self.tilemap_image.subsurface(pg.Rect(tile_x, tile_y, self.tile_width, self.tile_height))

                if (tile_row, tile_col) in self.animated_tiles:
                    tile_image = self.animated_tiles[(tile_row, tile_col)][self.current_frame]

                display.blit(tile_image, (x, y))

    def update(self):
        self.update_animation()
