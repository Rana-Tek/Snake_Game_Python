# Main game file

import pygame

pygame.init()


# Screen size 
# We need to open a window for the game. Create a window using pygame's display module. Determine the size and title of the window. 
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Game title

pygame.display.set_caption("Snake Game")

# colors 

white = (255,255,255)
black = (0,0,0)

# Game Loop

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    
    screen.fill(black) # background color black
    pygame.display.update() # Screen update
    
pygame.quit()