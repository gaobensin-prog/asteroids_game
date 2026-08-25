from circleshape import CircleShape as cs
from constants import LINE_WIDTH as lw
import pygame
class Asteroid(cs):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, lw)
        
    def update(self,dt):
        self.position += (self.velocity * dt)

    def split(self):
        pass