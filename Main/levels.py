import pygame

import constants
import platforms

class Level():

    size = constants.SPRITE_SIZE
    platform_list = None
    enemy_list = None
    levelmap = None
    level = []

    background = None

    world_shift = 0
    level_limit = -1000

    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.player = player

    def update(self):
        #update everything in the level
        self.platform_list.update()
        self.enemy_list.update()
        print("levels.worldd_shift", self.world_shift)

    def draw(self, screen):
        #draw everything in the level

        #draw background
        screen.fill(constants.BLUE)
        screen.blit(self.background, (self.world_shift // 3,0))

        #draw sprites
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)

    def shift_world(self, shift_x):

        self.world_shift += shift_x

        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):
    
    def __init__(self, player):
        Level.__init__(self, player)

        self.levelmap = pygame.image.load("leveltest.png").convert()
        self.background = pygame.image.load("achtergrond.png").convert()
        #self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1300

        for x in range(0, 140):
            for y in range(0, 40):
                currentPixel = self.levelmap.get_at((x, y))
                if currentPixel != (255, 255, 255, 255):
                    if currentPixel == (0, 255, 0, 255):
                        self.level.append([platforms.DIRT, (x * self.size), (y * self.size)])
                    if currentPixel == (255, 0, 0, 255):
                        self.level.append([platforms.STONE, (x * self.size), (y * self.size)])
                    if currentPixel == (255, 10, 0, 255):
                        self.level.append([platforms.CRACKED_STONE, (x * self.size), (y * self.size)])
                    if currentPixel == (255, 20, 0, 255):
                        self.level.append([platforms.DIRT_GRASS, (x * self.size), (y * self.size)])
                        

        for platform in self.level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Add a moving platform
        block = platforms.MovingPlatform(platforms.DIRT)
        block.rect.x = 600
        block.rect.y = 450
        block.boundary_left = 400
        block.boundary_right = 700
        block.change_x = 1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
