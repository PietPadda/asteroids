# constants.py

SCREEN_WIDTH = 1280  # window width
SCREEN_HEIGHT = 720  # window height

ASTEROID_MIN_RADIUS = 20  # min astrd radius
ASTEROID_KINDS = 3  # types of asteroid sizes, chose randomly in asteroidfield.py
ASTEROID_SPAWN_RATE = 0.8  # seconds per new spawn
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # max astrd radius

FPS = 60  # set game update/render frame rate

PLAYER_RADIUS = 20  # player hitbox circle size
PLAYER_TURN_SPEED = 300  # player rotation speed
PLAYER_SPEED = 200  # player straight/back speed
PLAYER_SHOOT_SPEED = 500  # speed of bullet flying
PLAYER_SHOOT_COOLDOWN = 0.3  # shoot cooldown timer

SHOT_RADIUS = 5  # bullet circle radius