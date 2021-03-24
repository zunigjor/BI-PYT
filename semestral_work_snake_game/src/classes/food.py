import pygame
import random

from semestralka.src.config import gameconfig as gc


class Food:
    """Food class."""
    def __init__(self):
        """Food constructor"""
        self.position = (0, 0)
        self.color = gc.COLOR_RED
        self.random_position()

    def get_postion(self):
        return self.position

    def random_position(self):
        """Move food to random position"""
        self.position = (random.randint(0, gc.GRID_WIDTH-1) * gc.SQUARE_SIZE,
                         random.randint(0, gc.GRID_HEIGHT-1) * gc.SQUARE_SIZE)

    def draw(self, surface):
        """Draw food"""
        r = pygame.Rect((self.position[0]+6, self.position[1]+6), (gc.SQUARE_SIZE - 12, gc.SQUARE_SIZE - 12))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, gc.COLOR_BLACK, r, 1)
