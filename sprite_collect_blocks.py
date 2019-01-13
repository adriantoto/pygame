"""
Use sprites to collect blocks.

Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Explanation video: http://youtu.be/4W2AqUetBi4
"""

# Libraries
import pygame
import sys
import random

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    """
        This class represents the ball.
        It derives from the "Sprite" class in pygame.
    """
    def __init__(self, color, width, height):
        """
            Constructor. Pass in the color of the block, and its size.
        """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting values of rect.x and rect.y
        self.rect = self.image.get_rect()

def main():
    """ Main function for the game. """
    pygame.init()

    # Set the width and height of the screen [width,height]
    screen_width = 700
    screen_height = 400
    screen = pygame.display.set_mode([screen_width, screen_height])

    pygame.display.set_caption("My Game")

    # This is a list of 'sprites'.
    # Each block in the program is added to this list. The list is managed by a class called 'Group'.
    block_list = pygame.sprite.Group()

    # This is a list of every sprite.
    # All blocks and the player block as well.
    all_sprites_list = pygame.sprite.Group()

    for i in range(50):
        # This represents a block
        block = Block(BLACK, 20, 15)

        # Set a random location for the block
        block.rect.x = random.randrange(screen_width)
        block.rect.y = random.randrange(screen_height)

        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

    # Create a RED player block
    player = Block(RED, 20, 15)
    all_sprites_list.add(player)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # Declare score.
    score = 0

    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # Close the window and quit.
                pygame.quit()
                sys.exit()
                quit()

        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

        # Get the current mouse position. This returns the position as a list of two numbers
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list (just like we'd fetch letters out of string.)
        # Set the player object to the mouse location
        player.rect.x = pos[0]
        player.rect.y = pos[1]

        # See if the player block has collided with anything.
        blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Check the list of collisions.
        for block in blocks_hit_list:
            score += 1
            print(score)

        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(WHITE)

        # Draw all the sprites
        all_sprites_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    main()
