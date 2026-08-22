import pygame
from constants import SCREEN_WIDTH as sw, SCREEN_HEIGHT as sh
from logger import log_state

def main():
    pygame.init()
    screen = pygame.display.set_mode((sw, sh))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {sw}")
    print(f"Screen height: {sh}")
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
