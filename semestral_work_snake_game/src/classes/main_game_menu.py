import pygame
import sys

from semestralka.src.config import gameconfig as gc
from semestralka.src.classes import game
from semestralka.src.classes import AI_game
from semestralka.src.classes import controls_screen


class MainGameMenu:
    """Main game menu class, from here the user can select what to do."""
    def __init__(self):
        """Main menu constructor"""
        self.running = True
        self.selection = 0
        self.options = ("Play", "Auto Play", "Controls", "Exit")
        self.title = "SNAKE"
        self.max_option = 3

        self.bg_color = gc.COLOR_LIGHT_BLUE
        self.selection_color = gc.COLOR_RED
        self.selection_bg_color = gc.COLOR_BLUE
        self.option_color = gc.COLOR_BLACK
        self.title_color = gc.COLOR_GREEN
        self.title_bg_color = gc.COLOR_BLACK

        self.screen = pygame.display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        self.font = pygame.font.SysFont("monospace", 50)
        self.title_font = pygame.font.SysFont("monospace", 100, True)

    def handle_events(self):
        """Handles user input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.selection -= 1
                    if self.selection < 0:
                        self.selection = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.selection += 1
                    if self.selection > self.max_option:
                        self.selection = self.max_option
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and self.selection == 0:
                    application = game.Game()
                    application.run()
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and self.selection == 1:
                    ai = AI_game.AIGame()
                    ai.run()
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and self.selection == 2:
                    controls = controls_screen.ControlsScreen()
                    controls.run()
                elif (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN) and self.selection == 3:
                    pygame.quit()
                    sys.exit()

    def render(self):
        """Renders menu on the screen"""
        self.screen.fill(self.bg_color)

        title_txt = self.title_font.render(self.title, True, self.title_color, self.title_bg_color)

        if self.selection == 0:
            op0 = self.font.render(self.options[0], True, self.selection_color, self.selection_bg_color)
        else:
            op0 = self.font.render(self.options[0], True, self.option_color)

        if self.selection == 1:
            op1 = self.font.render(self.options[1], True, self.selection_color, self.selection_bg_color)
        else:
            op1 = self.font.render(self.options[1], True, self.option_color)

        if self.selection == 2:
            op2 = self.font.render(self.options[2], True, self.selection_color, self.selection_bg_color)
        else:
            op2 = self.font.render(self.options[2], True, self.option_color)

        if self.selection == 3:
            op3 = self.font.render(self.options[3], True, self.selection_color, self.selection_bg_color)
        else:
            op3 = self.font.render(self.options[3], True, self.option_color)

        self.screen.blit(title_txt, ((gc.SCREEN_WIDTH / 2) - (title_txt.get_width() / 2), (gc.SCREEN_HEIGHT / 4)))
        self.screen.blit(op0, ((gc.SCREEN_WIDTH / 2) - (op0.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (-1 * 50)))
        self.screen.blit(op1, ((gc.SCREEN_WIDTH / 2) - (op1.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (0 * 50)))
        self.screen.blit(op2, ((gc.SCREEN_WIDTH / 2) - (op2.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (1 * 50)))
        self.screen.blit(op3, ((gc.SCREEN_WIDTH / 2) - (op3.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (2 * 50)))

        pygame.display.update()

    def run(self):
        """Main menu method, contains main loop"""
        while self.running:
            self.handle_events()
            self.render()
        return
