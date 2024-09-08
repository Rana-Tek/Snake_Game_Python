# Snake class and functions
# It contains a class that manages operations such as snake movement and growth. 

import pygame

class Snake:
    def __init__(self, color, initial_position, size):
        self.color = color
        self.size = size
        self.body = [initial_position] #snake body parts
        self.direction = pygame.K_RIGHT
        
    def move(self, x_change, y_change):
        #Adding new head position information of the snake
        new_head = (self.body[0][0] + x_change, self.body[0][1] + y_change)
        self.body = [new_head] + self.body[:-1]
        
    def grow(self):
        # Add new head to make snake bigger, keep tail fixed
        tail = self.body[-1]
        self.body.append(tail)
        
    def draw(self, screen):
        for part in self.body:
            pygame.draw.rect(screen, self.color, [part[0], part[1], self.size, self.size])
        
    
    def check_collision(self):
        #check if the snake hit its own body
        if len(self.body) > 1 and self.body[0] in self.body[1:]:
            return True
        return False
    
        
        