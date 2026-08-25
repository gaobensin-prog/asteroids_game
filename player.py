from circleshape import CircleShape
from constants import PLAYER_RADIUS as pr, PLAYER_TURN_SPEED as pts,PLAYER_SPEED,PLAYER_SHOOT_SPEED
import pygame
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,radius = pr)
        self.rotation = 0
    def rotate(self,dt):
        self.rotation += pts * dt
    def update(self,dt:float):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    def move(self,dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def shoot(self):
        shot=Shot(self.position[0],self.position[1])
        shot.velocity = pygame.math.Vector2.rotate(pygame.Vector2(0,1),self.rotation) * PLAYER_SHOOT_SPEED