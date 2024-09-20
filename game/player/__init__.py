import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.frame_width = 192
        self.frame_height = 192

        self.tilemap = pg.image.load("/Users/a./PycharmProjects/jogoEmPython/game/player/Warrior/Blue/Warrior_Blue.png").convert_alpha()

        self.idle_frames = self.load_frames(1, 1, 1, 6)
        self.walk_frames = self.load_frames(2, 1, 2, 6)
        self.attack_frames = self.load_frames(3, 1, 3, 6)

        self.current_animation = self.idle_frames
        self.current_frame = 0
        self.animation_speed = 0.1
        self.last_update = pg.time.get_ticks()

        self.image = self.current_animation[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (200, 100)

        self.velocity = 2
        self.facing_right = True

        self.attacking = False

    def load_frames(self, start_row, start_col, end_row, end_col):
        frames = []
        for row in range(start_row - 1, end_row):
            for column in range(start_col - 1, end_col):
                x = column * self.frame_width
                y = row * self.frame_height
                frame = self.tilemap.subsurface(pg.Rect(x, y, self.frame_width, self.frame_height))
                frames.append(frame)
        return frames

    def update_animation(self):
        now = pg.time.get_ticks()
        if now - self.last_update > 1000 * self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.current_animation)
            self.image = self.current_animation[self.current_frame]

            if not self.facing_right:
                self.image = pg.transform.flip(self.image, True, False)

    def move(self, key):
        if not self.attacking:
            if key[pg.K_a] or key[pg.K_d] or key[pg.K_w] or key[pg.K_s]:
                self.current_animation = self.walk_frames

                if key[pg.K_a]:
                    self.rect.x -= self.velocity
                    if self.facing_right:
                        self.facing_right = False

                elif key[pg.K_d]:
                    self.rect.x += self.velocity
                    if not self.facing_right:
                        self.facing_right = True

                if key[pg.K_s]:
                    self.rect.y += self.velocity
                elif key[pg.K_w]:
                    self.rect.y -= self.velocity
            else:
                self.current_animation = self.idle_frames

        if key[pg.K_k] and self.attacking == False:
            self.attack()

    def attack(self):
        self.attacking = True
        self.current_animation = self.attack_frames
        self.current_frame = 0

    def update(self):
        self.update_animation()

        if self.attacking and self.current_frame == len(self.attack_frames) - 1:
            self.attacking = False
            self.current_animation = self.idle_frames

    def draw(self, display):
        display.blit(self.image, self.rect)
