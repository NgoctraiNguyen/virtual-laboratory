import pygame
from lab.chemicals import Chemical
from lab.reactions import Reaction

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Virtual Laboratory")
bg = pygame.image.load("src/assets/image/phonghoahoc.png")
screen.blit(bg, (0, 0))
# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic for mixing chemicals and triggering reactions would go here

    # Clear the screen
    # screen.fill(())

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()