import pygame
from constants import SCREEN_WIDTH as sw, SCREEN_HEIGHT as sh
from logger import log_state
from player import Player
def main():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
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
        updatable.update(dt)
        for things in drawable:
            things.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
