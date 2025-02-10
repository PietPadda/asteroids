# main.py

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *  # wildcard imports are bad, but fine for constants in this projet


def main():

    pygame.init()  # init pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # pygame method, make a gui display

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up sprite groups (empty for now)
    updatable = pygame.sprite.Group()  # objects that can update
    drawable = pygame.sprite.Group()  # all objects that can be rendered
    asteroids = pygame.sprite.Group()  # contains all asteroids
    shots = pygame.sprite.Group()  # contains all player bullets

    # Class variables (static fields) container, then container
    # Register groups with Player class
    Player.containers = (updatable, drawable)

    # Register groups with Shot class
    Shot.containers = (shots, updatable, drawable)

    # Register groups with Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

    # no rendering, only updates. manages asteroids
    AsteroidField.containers = (updatable)

    # Create player in centre of screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create an AsteroidField object
    asteroid_field = AsteroidField()

    # Setup game clcok
    clock = pygame.time.Clock()  # create an clock object to set frame rate
    dt = 0  # delta time in seconds
    
    # Main game loop
    while True:
        # Handle window close
        for event in pygame.event.get():  # check if button pressed
            if event.type == pygame.QUIT:  # if X on window is pressed
                return  # exit the game
            
        screen.fill("black")  # black screen

        # update all updatable models model
        updatable.update(dt)  # call update method to allow rotation -- must be BEFORE draw...

        # after update positions, do collision check of asteroids v player
        for asteroid in asteroids:
            if asteroid.collision(player):  # check all asteroids v player
                print("Game Over!")  # last bit of text...
                return  # exit game
            
        # after update positions, do collision check of asteroids v shot
        for asteroid in asteroids:  # loop asteroids
            for shot in shots:  # loop shots
                if asteroid.collision(shot):  # check all asteroids v shot
                    asteroid.kill()  # remove asteroid from group
                    shot.kill()  # remove shot from group (else piercing)

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)  # after filling to layer on top, before refreshing to stay

        pygame.display.flip()  # Update display

        dt = clock.tick(FPS) / 1000  # default miliseconds, convert to seconds, FPS to 60 from constants


# Only run the game if main is run directly
if __name__ == "__main__":
    main()