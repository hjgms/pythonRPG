import pygame as pg

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frame_width = 192
        self.frame_height = 192

        self.tilemap = pg.image.load("/Users/a./PycharmProjects/jogoEmPython/game/enemy/Goblins/Troops/Torch/Red/Torch_Red.png").convert_alpha()

        self.idle_frames = self.load_frames(1, 1, 1, 6)

        self.current_animation = self.idle_frames
        self.current_frame = 0
        self.animation_speed = 0.1
        self.last_update = pg.time.get_ticks()

        self.image = self.current_animation[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 100)

        self.velocity = 2
        self.facing_right = True

    def load_frames(self, start_row, start_col, end_row, end_col):
        frames = []
        for row in range(start_row - 1, end_row):
            for column in range(start_col - 1, end_col):
                x = column * self.frame_width
                y = row * self.frame_height
                frame = self.tilemap.subsurface(pg.Rect(x, y, self.frame_width, self.frame_height))
                frames.append(frame)
        return frames