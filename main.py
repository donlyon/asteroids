# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize all imported pygame modules
    pygame.init()

    # set the width and height of the screen [width, height]
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # --- Game logic should go here
        screen.fill("black")
        for thing in updatable:
            thing.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                return

        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        # --- Drawing code should go here
        for thing in drawable:
            thing.draw(screen)

        # --- Update the screen with what we've drawn
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
