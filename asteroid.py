from circleshape import CircleShape as cs
from constants import LINE_WIDTH as lw,ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random
class Asteroid(cs):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, lw)
        
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new1 = Asteroid(self.position[0],self.position[1],new_radius)
        new1.velocity = pygame.math.Vector2.rotate(self.velocity,angle) * 1.2
        new2 = Asteroid(self.position[0],self.position[1],new_radius)
        new2.velocity = pygame.math.Vector2.rotate(self.velocity,-angle) * 1.2