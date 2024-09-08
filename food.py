# bait class and 
# by creating baits and placing them in a random location on the screen

import pygame
import random

class Food:
    def __init__(self, color, screen_width, screen_height, size):
        self.color = color
        self.size = size
        self.position = self.generate_random_position(screen_width, screen_height)
        
        #DEBUG : check position
        print(f"Generated food position: {self.position}")
    
    def generate_random_position(self, screen_width, screen_height):
        # check that the screen dimensions are larger than the feed size
        if screen_width > self.size and screen_height > self.size:
            x = round(random.randrange(0, screen_width - self.size) / 10.0) * 10.0
            y = round(random.randrange(0, screen_height - self.size) / 10.0) * 10.0
            return(x, y)
        else:
            print(f"Error: Screen size is too small for food size.")
            return None
        
    def draw(self, screen):
        
        #pre-error checkpoint
        if self.position is not None:
            pygame.draw.rect(screen, self.color, [self.position[0], self.position[1], self.size, self.size])
        else:
            print(f"Error: Food position is None.")
        