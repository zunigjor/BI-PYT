import pygame

from semestralka.src.config import gameconfig as gc

class Snake:
    """Snake class"""
    def __init__(self):
        """Snake constructor."""
        self.length = 1
        self.positions = [((gc.SCREEN_WIDTH / 2), (gc.SCREEN_HEIGHT / 2))]
        self.direction = (0, 0)
        self.head_color = gc.COLOR_DARK_GREEN
        self.body_color = gc.COLOR_GREEN

    def get_head(self):
        """Returns the position of the snake's head"""
        return self.positions[0]

    def get_tail(self):
        """Returns the postion of the snake's tail"""
        return self.positions[-1]

    def turn(self, point):
        """
        Sets the direction of the snake.
        If the snake is longer than 1 it cannot turn back into itself.
        """
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self) -> bool:
        """Moves the snake"""
        cur = self.get_head()
        x, y = self.direction
        new = (((cur[0] + (x * gc.SQUARE_SIZE)) % gc.SCREEN_WIDTH),
               ((cur[1] + (y * gc.SQUARE_SIZE)) % gc.SCREEN_HEIGHT))
        if len(self.positions) > 1 and new in self.positions:
            return False
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return True

    def reset(self):
        """Resets the snake"""
        self.length = 1
        self.positions = [((gc.SCREEN_WIDTH / 2), (gc.SCREEN_HEIGHT / 2))]
        self.direction = (0, 0)

    def draw(self, surface):
        """Draws the snake"""
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gc.SQUARE_SIZE, gc.SQUARE_SIZE))
            if p == self.get_head():
                pygame.draw.rect(surface, self.head_color, r)
            else:
                pygame.draw.rect(surface, self.body_color, r)
            pygame.draw.rect(surface, gc.COLOR_BLACK, r, 1)

    def handle_input(self, event):
        """Handles input"""
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.turn(gc.UP)
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.turn(gc.DOWN)
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.turn(gc.LEFT)
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.turn(gc.RIGHT)
