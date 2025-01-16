import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(color = "white", surface = screen,center = self.position, radius = PLAYER_SHOT_RADIUS, width = 2 )

    def update(self, dt):
        self.position += self.velocity #* dt


