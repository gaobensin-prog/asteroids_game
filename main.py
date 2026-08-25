import pygame
from constants import SCREEN_WIDTH as sw, SCREEN_HEIGHT as sh
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,drawable,updatable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    field=AsteroidField()
    player=Player(sw/2, sh/2)
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((sw, sh))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {sw}")
    print(f"Screen height: {sh}")
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)
        for thing in asteroids:
            if thing.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for bullet in shots:
                if bullet.collides_with(thing):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(thing)
                    pygame.sprite.Sprite.kill(bullet)

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
