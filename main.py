# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()  # init pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # new gui
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        # close window check
        for event in pygame.event.get():  # check if button pressed
            if event.type == pygame.QUIT:  # if X on window is pressed
                return  # exit the game
        screen.fill((0,0,0))  # pygame method, fill screen with RGB "black"
        pygame.display.flip()  # pygame method, refresh the sccreen


# Only run the game if main is run directly
if __name__ == "__main__":
    main()