# helping game functions

import pygame

def check_collision(snake, food):
    # Check if the snake collides with the bait
    if snake.body[0] == food.position:
        return True
    return False

def check_wall_collision(snake, screen_width, screen_height):
    # If the snake hits the wall it returns True
    x, y = snake.body[0]
    if x >= screen_width or x < 0 or y >= screen_height or y < 0:
        return True
    return False