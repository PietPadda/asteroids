import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x , y):
        super().__init__(x, y, PLAYER_RADIUS)  # inherit from parent
        self.rotation = 0  # init angle at 0°

    def triangle(self):
        # forward vector points in ship's current direction (based on rotation)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # (0,1) points straight down (+y = down)
        # right vector is perpendicular to forward (rotation + 90) and scaled for width
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # calculate triangle vertices
        a = self.position + forward * self.radius      # nose of ship
        b = self.position - forward * self.radius - right  # bottom left
        c = self.position - forward * self.radius + right  # bottom right
        
        return [a, b, c]
    
    # Override parent's draw method to render a triangle instead of a circle
    def draw(self, screen):
        LINE_WIDTH = 2  # line width of triangle
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)  # draw polygon
        # first calls object to draw, then colour, then coordinates, then LW