import pygame
import sys

from semestralka.src.classes import snake
from semestralka.src.classes import food
from semestralka.src.classes import victory_screen
from semestralka.src.config import gameconfig as gc


class Game:
    """PLayer game class"""
    def __init__(self):
        """Game class constructor"""
        self.running = True
        self.paused = False
        self.score = 0
        self.high_score = 0
        self.game_speed = 6
        self.snake = snake.Snake()
        self.food = food.Food()
        self.moves = 0

        self.tile1_color = gc.COLOR_LIGHT_BLUE
        self.tile2_color = gc.COLOR_BLUE
        self.score_text_color = gc.COLOR_BLACK
        self.pause_text_color = gc.COLOR_RED

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        self.font = pygame.font.SysFont("monospace", 25)
        self.pause_font = pygame.font.SysFont("monospace", 40, True)

    def draw_grid(self):
        """Draws a grid as background"""
        for y in range(0, int(gc.GRID_HEIGHT)):
            for x in range(0, int(gc.GRID_WIDTH)):
                if (x + y) % 2 == 0:
                    r = pygame.Rect((x * gc.SQUARE_SIZE, y * gc.SQUARE_SIZE), (gc.SQUARE_SIZE, gc.SQUARE_SIZE))
                    pygame.draw.rect(self.surface, self.tile1_color, r)
                else:
                    r = pygame.Rect((x * gc.SQUARE_SIZE, y * gc.SQUARE_SIZE), (gc.SQUARE_SIZE, gc.SQUARE_SIZE))
                    pygame.draw.rect(self.surface, self.tile2_color, r)

    def handle_events(self):
        """Input handle."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_p:
                    self.paused = not self.paused
                else:
                    self.snake.handle_input(event)
                    return  # prevents a bug where the snake turns into himself after a fast press of two keys

    def update(self):
        """Update objects."""
        if not self.snake.move():
            self.high_score = max(self.score, self.high_score)
            self.snake.reset()
            self.moves = 0
            self.score = 0
            self.food.random_position()
            while self.food.position in self.snake.positions:  # prevents food to spawn inside the snake
                self.food.random_position()

        self.moves += 1
        if self.snake.get_head() == self.food.position:
            self.snake.length += 1
            self.score += 1
            if self.score == gc.MAX_SCORE:
                victory = victory_screen.VictoryScreen(self.moves)
                victory.run()
                self.running = False
                return
            while self.food.position in self.snake.positions:  # prevents food to spawn inside the snake
                self.food.random_position()


    def render(self):
        """Render objects."""
        self.draw_grid()

        self.snake.draw(self.surface)
        self.food.draw(self.surface)

        self.screen.blit(self.surface, (0, 0))

        if self.score == 0:
            high_score_text = self.font.render("High score {0}".format(self.high_score), True, self.score_text_color)
            self.screen.blit(high_score_text, (gc.SCREEN_WIDTH - high_score_text.get_width() - 5, 5))
            score_text = self.font.render("Score {0}".format(self.score), True, self.score_text_color)
            self.screen.blit(score_text, (5, 5))
        else:
            score_text = self.font.render("{0}".format(self.score), True, self.score_text_color)
            self.screen.blit(score_text, (5, 5))
        if self.paused:
            pause_text = self.pause_font.render("PAUSED", True, self.pause_text_color)
            self.screen.blit(pause_text, (gc.SCREEN_WIDTH/2 - (pause_text.get_width() / 2), gc.SCREEN_HEIGHT/2))

        pygame.display.update()

    def run(self):
        """Main game method."""
        while self.running:
            self.clock.tick(self.game_speed)
            self.handle_events()
            if not self.paused:
                self.update()
            self.render()
        return
