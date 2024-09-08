# Main game file
# contains the main loop of the game and the initialization of the game. Import necessary classes and functions from other files.

import pygame
from snake import Snake
from food import Food
import config
import game_functions as gf


pygame.init()

screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Snake Games")

clock = pygame.time.Clock()

snake = Snake(config.WHITE, (300, 200), config.SNAKE_SIZE)
food = Food(config.RED, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SNAKE_SIZE)

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.direction != pygame.K_RIGHT:
                snake.direction = pygame.K_LEFT
            if event.key == pygame.K_RIGHT and snake.direction != pygame.K_LEFT:
                snake.direction = pygame.K_RIGHT
            if event.key == pygame.K_UP and snake.direction != pygame.K_DOWN:
                snake.direction = pygame.K_UP
            if event.key == pygame.K_DOWN and snake.direction != pygame.K_UP:
                snake.direction = pygame.K_DOWN
                
    
    if snake.direction == pygame.K_LEFT:
        x_change = -config.SNAKE_SPEED
        y_change = 0
    elif snake.direction == pygame.K_RIGHT:
        x_change = config.SNAKE_SPEED
        y_change = 0
    elif snake.direction == pygame.K_UP:
        x_change = 0
        y_change = -config.SNAKE_SPEED
    elif snake.direction == pygame.K_DOWN:
        x_change = 0
        y_change = config.SNAKE_SPEED
    
    snake.move(x_change, y_change)
    
    if gf.check_collision(snake, food):
        snake.grow()
        snake.move(x_change, y_change)
        food = Food(config.RED, config.SCREEN_WIDTH, config.SCREEN_HEIGHT, config.SNAKE_SIZE)
        
    
    #Let's check whether the snake hit the wall and whether it hit itself
    if gf.check_wall_collision(snake, config.SCREEN_WIDTH, config.SCREEN_HEIGHT):
        print("Yılan duvara çarptı")
        game_over = True
    elif snake.check_collision():
        print("Yılan kendine çarptı")
        print(f"Yılanın pozisyonu: {snake.body}")
        game_over = True
    
    
    
  #  if gf.check_wall_collision(snake, config.SCREEN_WIDTH, config.SCREEN_HEIGHT) or snake.check_collision():
   #     game_over = True
    
    
    screen.fill(config.BLACK)
    snake.draw(screen)
    food.draw(screen)
    pygame.display.update()
    
    clock.tick(10)


pygame.quit()







#( basic consepts 
# pygame.init()
# Screen size 
# We need to open a window for the game. Create a window using pygame's display module. Determine the size and title of the window. 
# screen_width = 600
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))

# Game title

# pygame.display.set_caption("Snake Game")

# colors 

#white = (255,255,255)
#black = (0,0,0)

# Game Loop

#game_over = False
#while not game_over:
 #   for event in pygame.event.get():
  #      if event.type == pygame.QUIT:
   #         game_over = True
    
   # screen.fill(black) # background color black
   # pygame.display.update() # Screen update
    
#pygame.quit() )