# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *  # wildcard imports are bad, but fine for constants in this projet



def main():

    pygame.init()  # init pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # pygame method, make a gui display

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()  # create an clock object to set frame rate
    dt = 0  # delta time to decouple game's speed from drawing speed
    
    while True:
        # close window check
        for event in pygame.event.get():  # check if button pressed
            if event.type == pygame.QUIT:  # if X on window is pressed
                return  # exit the game
        screen.fill((0,0,0))  # pygame method, fill screen with RGB "black"
        pygame.display.flip()  # pygame method, refresh the sccreen

        dt = clock.tick(FPS) / 1000  # default miliseconds, convert to seconds, FPS to 60 from constants


# Only run the game if main is run directly
if __name__ == "__main__":
    main()