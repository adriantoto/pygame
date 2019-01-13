# libraries
import pygame
import sys
import math
import random

# initialize the game engine
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Opening and settings the windows size
size = (400, 400)
screen = pygame.display.set_mode(size) #more : http://www.pygame.org/docs/ref/display.html

# Setting the window title
pygame.display.set_caption("Snow Animation")

# Setting up the main program loop
#Loop until the user click the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create an empty array
snow_list = []

# Loop 50 times and add a snow flake in a random x,y position
for i in range(50):
    x = random.randrange(0, 400)
    y = random.randrange(0, 400)
    snow_list.append([x, y])

#------------------Main Program Loop---------------------

while not done:
    #----Main event loop
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT: #If user clicked close
            done == True #flag that we are done so we exit this loop
            # Proper shutdown of a Pygame program
            pygame.quit()
            sys.exit()
            quit()

    #----Game logic should go here


    #----Drawing code should go here

    """First, clear the screen to white, Don't put other drawing commands.
    above this, or they will be erased with this command."""
    screen.fill(BLACK)

    # Process each snow flake in the list
    for i in range(len(snow_list)):

        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        # Move the snow flake down one pixel
        snow_list[i][1] += 1

        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 400:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 400)
            snow_list[i][0] = x

    #----Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    #----Limit to 60 fps
    clock.tick(60)
