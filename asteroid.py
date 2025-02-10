# asteroid.py

import pygame
import random
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

    def split(self):
        self.kill()  # rm obj
        if self.radius <= ASTEROID_MIN_RADIUS:  # if smallest asteroid
            return  # don't split
        # Split logic for asteroid
        random_angle = random.uniform(20, 50)  # random new angle for split astds
        vec_spl1 = self.velocity.rotate(random_angle)  # move vector for split 1
        vec_spl2 = self.velocity.rotate(-random_angle)  # move vector for split 2
        radius_spl = self.radius - ASTEROID_MIN_RADIUS  # new split radius
        asteroid1 = Asteroid(self.position.x, self.position.y, radius_spl)  # create astrd1
        asteroid2 = Asteroid(self.position.x, self.position.y, radius_spl)  # create astrd2
        asteroid1.velocity = vec_spl1 * 1.2  # modify astrd1 vel
        asteroid2.velocity = vec_spl2 * 1.2  # modify astrd1 vel


    def update(self, dt):
        # velocity is already a vector with direction and magnitude
        # just multiply it by dt to get the movement for this frame
        self.position += self.velocity * dt  # modify position relative to vector * parent speed * time
