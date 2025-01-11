import constants # suggested : from constants import * 
import pygame
from player import Player








def main():

    print("Starting asteroids!")
    pygame_inits = pygame.init()
    print(pygame_inits)
    game_clock = pygame.time.Clock()
    dt = 0
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    # https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(screen)

    player = Player(y = constants.SCREEN_HEIGHT / 2, x = constants.SCREEN_WIDTH / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000 # see https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick


        




if __name__ == "__main__":
    main()

