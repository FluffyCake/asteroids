import pygame
from constants import *
from player import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


    while True:
        screen.fill("black")
        player.update(dt)
        player.draw(screen)          
        pygame.display.flip()

        # kill the program if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
