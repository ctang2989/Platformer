# Pull sprites from sprite sheets

import pygame
import constants

class SpriteSheet(object):
    sprite_sheet = None

    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):

        image = pygame.Surface([width, height]).convert()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image.set_colorkey(constants.BLACK)

        return image