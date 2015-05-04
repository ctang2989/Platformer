import pygame

import constants

from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

    change_x = 0
    change_y = 0

    walking_frames_l = []
    walking_frames_r = []



    direction = "R"

    level = None

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("p1_walk.png")

        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 21, 30)
        #image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(26, 0, 21, 30)
        #image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)



        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(0, 0, 21, 30)
        image = pygame.transform.flip(image, True, False)
        #image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(26, 0, 21, 30)
        image = pygame.transform.flip(image, True, False)
        #image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)

        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        self.rect = self.image.get_rect()

    def update(self):
        # Move the player
        # Gravity
        self.calc_gray()

        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        if self.direction == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
        else:
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]

        # See if the player hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        # move up/down
        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x

        if self.change_x == 0:
            if self.direction == "L":
                self.image = self.walking_frames_l[0]
            else:
                self.image = self.walking_frames_r[0]

    def calc_gray(self):
        # Calculate effect of gravity
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .65

        # If on the ground
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6
        self.direction = "L"

    def go_right(self):
        self.change_x = 6
        self.direction = "R"

    def stop(self):
        self.change_x = 0

    def game_over(self):
        if self.rect.y < 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            constants.game_over = True
