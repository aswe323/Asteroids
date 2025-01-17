import random
from constants import *
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(color = "white", surface = screen,center = self.position, radius = self.radius, width = 2 )
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        print(self.velocity)
        self.kill()
        if (self.radius <= ASTEROID_MIN_RADIUS):
            return
        else:
            split_angle = random.uniform(20,50)
            negative_angle = split_angle * -1

            velocity_one = self.velocity.rotate(split_angle)
            velocity_two = self.velocity.rotate(negative_angle)

            small_radius = self.radius - ASTEROID_MIN_RADIUS

            faster_asteroid = Asteroid(self.position.x, self.position.y, small_radius)
            # while instatiated with velocity, that doesn't account for speed, this is why we use current velocity insted of the new object's one.
            faster_asteroid.velocity = velocity_one * 1.2

            slower_asteroid = Asteroid(self.position.x, self.position.y, small_radius)
            slower_asteroid.velocity = velocity_two * 1.2
            
#           super().containers.add(faster_asteroid)
#           super().containers.add(slower_asteroid)
#                   ^ tuple
#           AsteroidField.containers.add(faster_asteroid)
#           AsteroidField.containers.add(slower_asteroid)

