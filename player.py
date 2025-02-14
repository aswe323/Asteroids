import pygame
import constants
from shot import Shot
from circleshape import  CircleShape 

class Player(CircleShape):
    def __init__(self, x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
        self.fire_delay = 0

    def shoot(self):
        new_shot = Shot(x = self.position.x, y = self.position.y)
        new_shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * constants.PLAYER_SHOT_SPEED
        #this causes a funny bug so I kept it :D
        # this applies the shot velocity to the player making it go really fast
        # I name it the "ramming speed" bug 
        #new_shot.rotation = self.rotation #player rotation indicated the direction of the shot
        #new_shot.position = self.position

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
        if (self.fire_delay > 0):
            self.fire_delay -= dt
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
            #### this also updates the speed and velocity of the player for some reason Q_Q
            if (self.fire_delay > 0):
                pass
            else:
                self.fire_delay += constants.PLAYER_SHOT_DELAY
                self.shoot()
            # ?

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt

