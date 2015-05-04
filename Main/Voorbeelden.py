#Python Platform_scroller

class Level_03(Level):

    def __init__(self, player):

        Level.__init__(self, player)

        self.background = pygame.image.load("???").convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -1000

        level = [[platforms.STONE_PLATFORM_LEFT, 50, 50] ]

        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        # Moving platform Y
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)


        # Moving platform X
        block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
        block.rect.x = 1500
        block.rect.y = 300
        block.boundary_top = 100
        block.boundary_bottom = 550
        block.change_y = -1
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
