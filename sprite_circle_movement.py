# Libraries
import pygame
import sys
import random
import math

# Define some colors as global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Block(pygame.sprite.Sprite):
    """
        This class represents the ball that moves in circle.
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

        # The center of the sprite will orbit
        self.center_x = 0
        self.center_y = 0

        # Current angle in radians
        self.angle = 0

        # How far away from the center to the orbit, in pixels
        self.radius = 0

        # How fast to orbit in radians per frame
        self.speed = 0.05

    def update(self):
        """
            Update the ball's position.
        """
        # Calculate a new x, y
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y

        # Increase the angle in prep for the next round
        self.angle += self.speed

class Player(pygame.sprite.Sprite):
    """
        Class to represent the player
    """
    def __init__(self, color, width, height):
        """
            Create the player image
        """
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        """
            Set the user to be where the mouse is.
        """
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

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

        # Set a random center location for the block to orbit
        block.center_x = random.randrange(screen_width)
        block.center_y = random.randrange(screen_height)

        # Random radius from 10 to 200
        block.radius = random.randrange(10, 200)

        # Random start angle from 0 to 2pi
        block.angle = random.random() * 2 * math.pi

        # radians per frame
        block.speed = 0.008

        # Add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)

    # Create a RED player block
    player = Player(RED, 20, 15)
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

        # Calls update() method on every sprite in the list
        all_sprites_list.update()

        # See if the player block has collided with anything
        block_hit_list = pygame.sprite.spritecollide(player, block_list, True)

        # Check the list collisions
        for block in block_list:
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
