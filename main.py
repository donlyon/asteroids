# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # initialize all imported pygame modules
    pygame.init()

    # set the width and height of the screen [width, height]
    size = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(size)

    while True:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # --- Game logic should go here
        screen.fill("black")

        # --- Drawing code should go here

        # --- Update the screen with what we've drawn
        pygame.display.flip()

if __name__ == "__main__":
    main()
