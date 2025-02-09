# circleshape.py

import pygame

# Base class for circular game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # If the class has a "containers" attribute, pass it to the parent class
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            # Otherwise, just initialize the parent class normally
            super().__init__()

        # Position as a 2D vector (x, y)
        self.position = pygame.Vector2(x, y)
        # Velocity vector defaults to (0, 0)
        self.velocity = pygame.Vector2(0, 0)
        # Radius of the circle
        self.radius = radius

    # Placeholder method for rendering on the screen
    def draw(self, screen):
        # Sub-classes (e.g., specific game objects) should implement this
        pass

    # Placeholder method for updating the object's state
    def update(self, dt):
        # Sub-classes should define behavior based on dt (delta time)
        pass