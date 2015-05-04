import pygame

import constants
import levels

from player import Player


def main():

    pygame.init()

    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    player = Player()

    level_list = []
    level_list.append(levels.Level_01(player))

    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height - 70
    active_sprite_list.add(player)

    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if constants.game_over:
                    constants.game_over = False
                    main()
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        active_sprite_list.update()

        current_level.update()
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.right >= 500:
            diff = player.rect.right - 500
            player.rect.right = 500
            current_level.shift_world(-diff)
        # If the player gets near the left side, shift the world right (+x)
        if player.rect.left <= 120 and current_level.world_shift < 0:
            diff = 120 - player.rect.left
            player.rect.left = 120
            current_level.shift_world(diff)
        # If the player gets to the end of the level, go to the next level
        current_position = current_level.world_shift

        #print( current_position )
        #print( current_position , " . " , player.rect.x )
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        current_level.draw(screen)
        active_sprite_list.draw(screen)

        player.game_over()
        if constants.game_over:
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over.", True, constants.BLACK)
            x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, (x, y))
        

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
