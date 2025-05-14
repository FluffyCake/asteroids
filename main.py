import pygame, sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    # Create sprite groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        screen.fill("black")
        updateable.update(dt)
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("GAME OVER")
                sys.exit(1)
            
            for shot in shots:
                if asteroid.is_colliding(shot):
                    print("Hit!")
                    asteroid.split()
                    shot.kill()

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        # kill the program if the user closes the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        dt = clock.tick(60) /1000

if __name__ == "__main__":
    main()
