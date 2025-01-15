import pygame
import constants
from shot import Shot
from circleshape import  CircleShape 

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.__x = x
        self.__y = y
        self.rotation = 0

    def shoot(self):
        new_shot = Shot(x = self.__x, y = self.__y, radius = constants.PLAYER_SHOT_RADIUS)
        new_shot.velocity = pygame.Vector2(0,1)
        new_shot.rotation = self.rotation #player rotation indicated the direction of the shot

    def draw(self, screen):
        pygame.draw.polygon(surface = screen, color = "white", points = self.triangle(), width =  2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += constants.PLAYER_ROTATION_SPEED * dt
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            # ?
        if keys[pygame.K_d]:
            self.rotate(dt)
            # ?
        if keys[pygame.K_w]:
            self.move(dt)
            # ?
        if keys[pygame.K_s]:
            self.move(-dt)
            # ?
        if keys[pygame.K_SPACE]:
            self.shoot()
            # ?
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

