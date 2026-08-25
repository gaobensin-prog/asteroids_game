from circleshape import CircleShape
from constants import PLAYER_RADIUS as pr, PLAYER_TURN_SPEED as pts,PLAYER_SPEED,PLAYER_SHOOT_SPEED,PLAYER_SHOOT_COOLDOWN_SECONDS as cd
import pygame
from shot import Shot
class Player(CircleShape):
    def __init__(self,x,y,cooldown = 0):
        super().__init__(x,y,radius = pr)
        self.rotation = 0
        self.cooldown = cooldown

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
            self.cooldown -= dt
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
        if self.cooldown < 0:
            shot=Shot(self.position[0],self.position[1])
            shot.velocity = pygame.math.Vector2.rotate(pygame.Vector2(0,1),self.rotation) * PLAYER_SHOOT_SPEED
            self.cooldown = cd