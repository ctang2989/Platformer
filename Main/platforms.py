import pygame

from spritesheet_functions import SpriteSheet

DIRT = (0, 0, 15, 15)
CRACKED_STONE = (0, 16, 15, 15)
STONE = (16, 0, 15, 15)
DIRT_GRASS = (48, 0, 15, 15)


INVISIBLE_WALL = (1000, 1000, 1, 2000)

class Platform(pygame.sprite.Sprite):
    # Non-moving Platform
    def __init__(self, sprite_sheet_data):
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("mctile.png")

        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

class MovingPlatform(Platform):
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):
        # Moving the platform
        # Move left/right
        self.rect.x += self.change_x

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # Did hit the player. Move the player around and assume they won't hit anything else
            if self.change_x < 0:                           #moving right
                self.player.rect.right = self.rect.left
            else:                                           #moveing left
                self.player.rect.left = self.rect.right

        #move Up/Down
        self.rect.y += self.change_y

        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check boundaries and see if we need to reverse
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
