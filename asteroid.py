# asteroid.py

import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Override parent's draw method to render a circle
    def draw(self, screen):
        LINE_WIDTH = 2  # line width of circle
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)  # draw circle
        # first calls object to draw, colour, position, radius, then LW
        # position & radius are from parent init

    def update(self, dt):
        # velocity is already a vector with direction and magnitude
        # just multiply it by dt to get the movement for this frame
        self.position += self.velocity * dt  # modify position relative to vector * parent speed * time
