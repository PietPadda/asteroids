# asteroids

Running guide:
1) open main.py in VS Code
2) source venv/bin/activate  --> opens virtual environment
3) python3 main.py --> runs the game!

Controls guide:
W/S = forwards/backwards
A/D = left/right rotation
Spacebar = shoot

Gameplay loop:
1) Avoid being hit by asteroids or it's game over!
2) Shoot the asteroids, but be careful: they split into smaller pieces
3) Good luck!

# Step-by-step building process below:

2.	Asteroids (After OOP via Python:):
1.	Pygame

Build an Asteroids Game:
•	bootdev upgrade   ensure Bootdev CLI is up to date

Installation:
•	Go to workspace/github.com/username/   will make a subfolder
•	Create a repo on github
•	git clone REPOLINK   will create an asteroids folder + initiate .git
•	file  open folder  asteroids  set the current project
•	Install VcXsrv to run pygame on WSL
•	sudo apt install python3.12-venv   install virtual environment for python 3.12
•	python3 -m venv venv   create a virtual environment in the asteroids folder
•	source venv/bin/activate   activate the virtual environment
•	Should see something like: (venv) wagslane@MacBook-Pro-2 asteroids %
•	Note: make sure that your virtual environment is activated when running the game or using the bootdev CLI.
•	nano requirements.txt  touch …  pygame==2.6.1  tells python to use this pygame version
•	pip install -r requirements.txt   install pygame to virtual environment
•	python3 -m pygame   ensure pygame is installed
•	Note: this will result in an error (the test expects an exit code of 1), but the output will show that pygame is installed.

Pygame:
•	touch main.py   let’s write some boilerplate code in vs studio

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

def main():
    print("Starting asteroids!")

# Only run the game if main is run directly
if __name__ == "__main__":
    main()

2.	Player:

Modules:
•	touch constants.py  where we’ll add all our game constants

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

•	from constants import SCREEN_WIDTH, SCREEN_HEIGHT  # usually bad to use * wildcard, fine for constants, explicit > implicit
•	update main to print width and height  use FILENAME. to access it

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

Game Loop:
•	while True:  initiate an infinite game loop
•	screen.fill((0,0,0))   fill pygame window with black RGB
•	pygame.display.flip()  refresh the window, Should see a black window appear on run now
•	ctrl + c  kills program
•	Add an event check at start of while, if X is pressed on window, close the game

# close window check
        for event in pygame.event.get():  # check if button pressed
            if event.type == pygame.QUIT:  # if X on window is pressed
                return  # exit the game

•	touch .gitignore  create file for git commit ignore list
•	nano and add “venv/” & “__pycache__/”  these are regenerated, can safely ignore. These are virtual environment folder + python’s cache folder
•	git status  check what has changed
•	git log --oneline –graph  check commit history log as oneline text & branching graph, nothing yet
•	git add .  add all “.” to commit list
•	git status  check what has changed (you’ll see all added all)
•	git commit -m “message for what has happened”  will create a commit request
•	git log --oneline –graph + git status  Log shows your commit(s). Status shows clean, nothing to commit
•	git push origin main  “git push” = upload local commit, “origin” default remote repo (Github.com), “main” = branch pushing to ie. “Send my committed changes to GitHub’s main branch”

FPS:
•	clock = pygame.time.Clock()  create a block object before game loop for fps limit
•	dt = 0  create a delta time to decouple game’s speed from drawing speed
•	dt = clock.tick(FPS) / 1000  add end of game loop, set frames per second constant to 60. Set dt equal and /1000 to convert time passed to seconds, default ms
Sprites:
•	touch circleshape.py

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

Draw Player:
•	PLAYER_RADIUS = 20  add to constants for player hitbox radius
•	Touch player.py
•	Player class inherits from CircleShape
•	Constr takes x, y, Player Radius
•	Initialise rotation to 0

import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS

class Player(CircleShape):
    def __init__(self, x , y):
        super().__init__(x, y, PLAYER_RADIUS)  # inherit from parent
        self.rotation = 0  # init angle at 0°

•	Add a triangle method to draw the ship
•	pygame.Vector2(0, 1)  sets 0 “motion” in x and 1 in y.
•	.rotate(self.rotation)  rotate method to change this vector by whatever the angle is
•	.rotate(self.rotation + 90)  makes it perpendicular
•	* self.radius / 1.5  it would be super short without * r, and be too “thick” if no /1.5 to make it better
•	 
•	For vertices, we’re calculating from the CENTRE point. So nose point is radius away from centre, both read points are radius away from centre in OTHER direction, then radius/1.5 in opposite

    def triangle(self):
        # forward vector points in ship's current direction (based on rotation)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # (0,1) points straight down (+y = down)
        # right vector is perpendicular to forward (rotation + 90) and scaled for width
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        
        # calculate triangle vertices
        a = self.position + forward * self.radius      # nose of ship, centre + down vector (R)
        b = self.position - forward * self.radius - right  # bottom left, centre – down vector (R) - side vector
        c = self.position - forward * self.radius + right  # bottom right, centre – down vector (R) + side vector
        
        return [a, b, c]

•	Override parent render method to draw triangle rather than circle

    # Override parent's draw method to render a triangle instead of a circle
    def draw(self, screen):
        LINE_WIDTH = 2  # line width of triangle
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)  # draw polygon
        # first calls object to draw, then colour, then coordinates, then LW

•	In main, create a player instance at centre of screen

from player import Player
...
    # instantiate a Player (ship) object
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)  # x/y to spawn in middle of screen

•	Let’s draw the player. After screen fill, before refresh. 1) Create background, 2) draw player, 3) render frame update. If player before background, would layer below… if frame before player, wouldn’t draw player…

        # draw player after
        player.draw(screen)  # after filling to layer on top, before refreshing to stay

Moving Around:
•	PLAYER_TURN_SPEED = 300  add to constants for player rotate method
•	Add rotate method to Player  will use dt as input with turn speed to update player rotation parameter

def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt  # turnspeed + time lapse = rotation change rate

•	Add an update method to Player, with rotation keys implemented

    def update(self, dt):
        keys = pygame.key.get_pressed()  # get keyboard input

        # rotate left
        if keys[pygame.K_a]:  # a button
            self.rotate(-dt)  # rotate left (ANTI clockwise)

        if keys[pygame.K_d]:  # d button
            self.rotate(dt)  # rotate right (clockwise)

•	Update main to call player update method

        # update character model
        player.update(dt)  # call update method to allow rotation -- must be BEFORE draw...

Moving:
•	PLAYER_SPEED = 200  add to constants for player forward/back speed
•	Create Player .move() method  this will allow moving forward and backwards
•	We start with a unit vector pointing straight up from (0, 0) to (0, 1).
•	We rotate that vector by the player’s rotation, so it’s pointing in the direction the player is facing.
•	We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
•	Add the vector to our position to move the player.
•	 

def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # vector, with rotation to align with render rotation
        self.position += forward + PLAYER_SPEED * dt  # modify position relative to vector * speed change over time

•	Add w & s keys to the .update() method in player

        # move forward
        if keys[pygame.K_w]:  # w button
            self.move(dt)  # rotate left (ANTI clockwise)

        # move back
        if keys[pygame.K_s]:  # s button
            self.move(-dt)  # rotate right (clockwise)

Groups:
•	Organise different objects via groups to handle different move(), draw() etc. calls
•	 
•	Create sprite groups (empty for now)

    # Set up sprite groups (empty for now)
    updatable = pygame.sprite.Group()  # objects that can update
    drawable = pygame.sprite.Group()  #all objects that can be rendered

•	Create group container, helps automatically add all player objects to join both groups

    # Class variables (static fields) container, then container
    # Register groups with Player class
    Player.containers = (updatable, drawable)

•	Change update and draw calls to now work on the groups rather than just the player object

        # update all updatable models model, must be before filling the screen...
        updatable.update(dt)  # call update method to allow rotation -- must be BEFORE draw...

        # Draw all sprites
        for sprite in drawable:
            sprite.draw(screen)  # after filling to layer on top, before refreshing to stay

3.	Asteroids:

Asteroids:
•	touch asteroid.py
•	create Asteroid class that inherits from CircleShape

# asteroid.py

import pygame
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

•	override asteroid draw(), to draw a circle for asteroid

    # Override parent's draw method to render a circle
    def draw(self, screen):
        LINE_WIDTH = 2  # line width of circle
        pygame.draw.circle(screen, "white", (self.x, self.y), self.radius, LINE_WIDTH)  # draw circle
        # first calls object to draw, colour, coordinates, radius, then LW

•	override asteroid update, must move in straight line and use CircleShape inherited self.velocity

    def update(self, dt):
        # velocity is already a vector with direction and magnitude
        # just multiply it by dt to get the movement for this frame
        self.position += (self.velocity * dt)  # modify position relative to vector * parent speed * time

•	add asteroids group to main + update static containers field

    asteroids = pygame.sprite.Group()  # contains all asteroids
    ...
    # Register groups with Asteroid class
    Asteroid.containers = (asteroids, updatable, drawable)

•	touch asteroidfield.py, use code provided (I added comments for clarity)

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

•	add an asteroidfield container in main, no rendering needed

    # no rendering, only updates. manages asteroids
    AsteroidField.containers = (updatable)

•	add an object in main

    # Create an AsteroidField object
    asteroid_field = AsteroidField()

Collisions:
•	We calculate the distance between the center of the two circles, let’s call it distance
•	Let’s call the radius of one circle r1, and the radius of the other circle r2
•	If distance is less than or equal to r1 + r2, the circles are colliding. If not, they aren’t.
•	 
•	Create a collision method in CircleShape (all objs are “circles”):
•	CircleShape defines positions as vectors, we can thus use SELF.VAR.distance_to(OTHER.VAR) for dist!

    # collision detection between circles
    def collision(self, object):  # circleshape objects
        distance = self.position.distance_to(object.position)  # measure dist btwn 2 vectors (.position is a vector)
        if distance <= self.radius + object.radius:  # check if dist >= r1+r2 of circles
            return True  # collision has occured
        else:
            return False  # no collision

•	After update in main (need positions), loop through all astrds and check collision with player

        # after update positions, do collision check of asteroids v player
        for asteroid in asteroids:
            if asteroid.collision(player):  # check all asteroids v player
                print("Game Over!")  # last bit of text...
                return  # exit game

Shooting:
•	touch shot.py. Same as asteroid.py, but uses SHOT_RADIUS = 5 for size
•	add main group for shots

    shots = pygame.sprite.Group()  # contains all player bullets

•	add PLAYER_SHOOT_SPEED = 500 to constants
•	In player, add a shoot() method

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)  # create Shot obj at player position
        forward = pygame.Vector2(0, 1).rotate(self.rotation)  # direct vector, w rotation to align w render rotation
        shot.velocity = forward * PLAYER_SHOOT_SPEED  # define shot velocity as vector * constant

•	Add spacebar as key input in update

         # shoot
        if keys[pygame.K_SPACE]:  # spacebar
            self.shoot()

•	add shot group and container

    shots = pygame.sprite.Group()  # contains all player bullets
...
    # Register groups with Shot class
    Shot.containers = (shots, updatable, drawable)

Rate Limit:
•	add a shoot timer under player init

        self.shoot_timer = 0  # init at 0s

•	in player shot(), defined the timer = PLAYER_SHOOT_COOLDOWN (0.3 in constants) and prevent shooting if timer > 0:

        if self.shoot_timer > 0:  # if cooldown timer still > 0
            return  # prevent shoot

        self.shoot_timer = PLAYER_SHOOT_COOLDOWN  # from 0 to cooldown duration

•	in player update(), decrement the timer until no longer > 0s

        if self.shoot_timer > 0:  # if a shot has fired
            self.shoot_timer -= dt  # decrease by dt with each update

Destruction:
•	add a shot v asteroid collision check, if true use .kill() pygame method to remove the objects!

        # after update positions, do collision check of asteroids v shot
        for asteroid in asteroids:  # loop asteroids
            for shot in shots:  # loop shots
                if asteroid.collision(shot):  # check all asteroids v shot
                    asteroid.kill()  # remove asteroid from group
                    shot.kill()  # remove shot from group (else piercing)

Splitting:
•	build a basic asteroid split method

    def split(self):
        self.kill()  # rm obj
        if self.radius <= ASTEROID_MIN_RADIUS:  # if smallest asteroid
            return  # don't split

•	now for respawn logic
•	 
•	import random
•	blue angle = random.uniform between 20 & 50 deg
•	let’s update the split method: don’t respawn if already at smallest. If not, use random angle, modify 2 velocity vectors, calculate a new smaller radius, spawn 2 asteroids, and apply 2 new velocity vectors to them

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

•	Finally, replace the man update from kill to split (else won’t split…)

        # after update positions, do collision check of asteroids v shot
        for asteroid in asteroids:  # loop asteroids
            for shot in shots:  # loop shots
                if asteroid.collision(shot):  # check all asteroids v shot
                    asteroid.split()  # SPLIT asteroid
                    shot.kill()  # remove shot from group (else piercing)
