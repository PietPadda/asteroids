# asteroidfield.py

import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    # Define spawn points and directions for asteroids around screen edges
    # Each edge is a list containing [direction_vector, position_calculator]
    edges = [
        # Right to left spawn: Asteroids appear on right edge, move left
        # Vector2(1,0) moves right, position starts at -radius and varies vertically
        [
            pygame.Vector2(1, 0),  # Direction vector pointing right
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),  # Spawn position
        ],
        # Left to right spawn
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        # Bottom to top spawn
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        # Top to bottom spawn
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Initialize sprite and add to container groups
        # containers is set in main.py to handle automatic group membership
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0  # Tracks time between asteroid spawns

    def spawn(self, radius, position, velocity):
        # Create new asteroid instance with given properties
        # position.x/y sets spawn location
        # radius determines asteroid size
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity  # Sets direction and speed of movement

    def update(self, dt):
        # Add elapsed time since last frame to spawn timer
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            # Reset timer when it's time to spawn
            self.spawn_timer = 0

            # Randomly select a spawn edge from the defined edges list
            edge = random.choice(self.edges)
            # Generate random speed between 40-100 pixels per second
            speed = random.randint(40, 100)
            # Calculate base velocity using edge direction * speed
            velocity = edge[0] * speed
            # Add some randomness to direction (-30 to +30 degrees)
            velocity = velocity.rotate(random.randint(-30, 30))
            # Calculate spawn position using edge's position function
            position = edge[1](random.uniform(0, 1))
            # Determine asteroid size (1 to ASTEROID_KINDS)
            kind = random.randint(1, ASTEROID_KINDS)
            # Spawn new asteroid with calculated properties
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)