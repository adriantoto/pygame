# libraries
import pygame
import sys
import math

# initialize the game engine
pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# Opening and settings the windows size
size = (700, 500)
screen = pygame.display.set_mode(size) #more : http://www.pygame.org/docs/ref/display.html

# Setting the window title
pygame.display.set_caption("pygame window")

# Setting up the main program loop
#Loop until the user click the close button
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the rectangle
rect_x = 50
rect_y = 50

# Speed and direction of rectangle
rect_change_x = 5
rect_change_y = 5

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

    # Bouncing a rectangle if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    #----Drawing code should go here
    
    """First, clear the screen to white, Don't put other drawing commands.
    above this, or they will be erased with this command."""
    screen.fill(WHITE)

    # Draw the rectangle
    pygame.draw.rect(screen, RED, [rect_x, rect_y, 50, 50])

    # Move the rectangle
    rect_x += rect_change_x
    rect_y += rect_change_y

    #----Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    #----Limit to 60 fps
    clock.tick(60)
