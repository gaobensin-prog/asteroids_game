from circleshape import CircleShape
from constants import PLAYER_RADIUS as pr, PLAYER_TURN_SPEED as pts
import pygame
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
            self.move(0)
        if keys[pygame.K_w]:
            self.move(dt)
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