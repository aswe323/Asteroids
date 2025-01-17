import constants # suggested : from constants import * 
import pygame
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField








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



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots,updatable, drawable)
    AsteroidField.containers = updatable

    astroidField = AsteroidField()
    Player.containers = (updatable, drawable) 

    updatable.add(player)
    drawable.add(player)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # apply
        for upd in updatable:
            upd.update(dt)

        # show 
        screen.fill("#000000")
        for dwa in drawable:
            dwa.draw(screen)

        for astroid in asteroids:
            if (astroid.collides_with(player)):
                print("game over!")
                pygame.QUIT
                return
        for astroid in asteroids:
            for shot in shots:
                if astroid.collides_with(shot):
                    shot.kill()
                    astroid.split()

        pygame.display.flip()
        dt = game_clock.tick(60) / 1000 # see https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick





        




if __name__ == "__main__":
    main()

