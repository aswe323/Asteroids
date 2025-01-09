import constants # suggested : from constants import * 
import pygame








def main():

    print("Starting asteroids!")
    pygame_inits = pygame.init()
    print(pygame_inits)
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")
    # https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    print(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("#000000")

        pygame.display.flip()




if __name__ == "__main__":
    main()

