import pygame
import sys
import pygame.locals

from semestralka.src.classes import snake
from semestralka.src.classes import food
from semestralka.src.classes import victory_screen
from semestralka.src.classes import ai
from semestralka.src.config import gameconfig as gc


class AIGame:
    """AI game class"""
    def __init__(self):
        """Game class constructor"""
        self.running = True
        self.paused = False
        self.score = 0
        self.game_speed = 10
        self.max_speed = 500
        self.min_speed = 10
        self.snake = snake.Snake()
        self.food = food.Food()
        self.moves = 0

        self.maze = ai.Maze()

        self.snake.head_color = gc.COLOR_ORANGE
        self.snake.body_color = gc.COLOR_YELLOW
        self.food.color = gc.COLOR_PINK

        self.tile1_color = gc.COLOR_DARK_BLUE
        self.tile2_color = gc.COLOR_DARKER_BLUE
        self.score_text_color = gc.COLOR_BLACK
        self.pause_text_color = gc.COLOR_RED

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        self.font = pygame.font.SysFont("monospace", 20)

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
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.game_speed += 10
                    if self.game_speed > self.max_speed:
                        self.game_speed = self.max_speed
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.game_speed -= 10
                    if self.game_speed < self.min_speed:
                        self.game_speed = self.min_speed

    def update(self):
        """Update objects."""
        # Get new snake direction
        direction = ai.get_new_direction(self.snake, self.food, self.maze)
        ai_event = pygame.event.Event(pygame.locals.KEYDOWN)
        if direction == gc.UP:
            ai_event.key = pygame.K_w
            self.snake.handle_input(ai_event)
        if direction == gc.DOWN:
            ai_event.key = pygame.K_s
            self.snake.handle_input(ai_event)
        if direction == gc.LEFT:
            ai_event.key = pygame.K_a
            self.snake.handle_input(ai_event)
        if direction == gc.RIGHT:
            ai_event.key = pygame.K_d
            self.snake.handle_input(ai_event)

        # Check collisions
        if not self.snake.move():
            self.running = False
            return
        self.moves += 1
        # Check if snake ate food
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

        score_text = self.font.render("Score {0}".format(self.score), True, self.score_text_color)
        speed_text = self.font.render("Speed {0}".format(self.game_speed), True, self.score_text_color)
        self.screen.blit(score_text, (5, 5))
        self.screen.blit(speed_text, (gc.SCREEN_WIDTH - speed_text.get_width() - 5, 5))

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
