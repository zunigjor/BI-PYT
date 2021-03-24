import pygame
import sys

from semestralka.src.config import gameconfig as gc


class ControlsScreen:
    """Controls screen"""
    def __init__(self):
        """Controls screen constructor"""
        self.running = True
        self.text = ("W - UP", "S - DOWN", "A - LEFT", "D - RIGHT", "P - PAUSE", "ESC - EXIT TO MAIN MENU")
        self.title = "SNAKE"

        self.bg_color = gc.COLOR_LIGHT_BLUE
        self.text_color = gc.COLOR_BLACK
        self.text_bg_color = gc.COLOR_BLUE
        self.title_color = gc.COLOR_GREEN
        self.title_bg_color = gc.COLOR_BLACK

        self.screen = pygame.display.set_mode((gc.SCREEN_WIDTH, gc.SCREEN_HEIGHT), 0, 32)
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()
        self.font = pygame.font.SysFont("monospace", 40)
        self.title_font = pygame.font.SysFont("monospace", 100, True)

    def handle_events(self):
        """Handles input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def render(self):
        self.screen.fill(self.bg_color)

        title_txt = self.title_font.render(self.title, True, self.title_color, self.title_bg_color)

        text0 = self.font.render(self.text[0], True, self.text_color, self.text_bg_color)
        text1 = self.font.render(self.text[1], True, self.text_color, self.text_bg_color)
        text2 = self.font.render(self.text[2], True, self.text_color, self.text_bg_color)
        text3 = self.font.render(self.text[3], True, self.text_color, self.text_bg_color)
        text4 = self.font.render(self.text[4], True, self.text_color, self.text_bg_color)
        text5 = self.font.render(self.text[5], True, self.text_color, self.text_bg_color)

        self.screen.blit(text0, ((gc.SCREEN_WIDTH / 2) - (text0.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (-2 * 40)))
        self.screen.blit(text1, ((gc.SCREEN_WIDTH / 2) - (text1.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (-1 * 40)))
        self.screen.blit(text2, ((gc.SCREEN_WIDTH / 2) - (text2.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (0 * 40)))
        self.screen.blit(text3, ((gc.SCREEN_WIDTH / 2) - (text3.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (1 * 40)))
        self.screen.blit(text4, ((gc.SCREEN_WIDTH / 2) - (text4.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (2 * 40)))
        self.screen.blit(text5, ((gc.SCREEN_WIDTH / 2) - (text5.get_width() / 2), (gc.SCREEN_HEIGHT / 2) + (3 * 40)))

        self.screen.blit(title_txt, ((gc.SCREEN_WIDTH / 2) - (title_txt.get_width() / 2), (gc.SCREEN_HEIGHT / 4)))

        pygame.display.update()

    def run(self):
        """Main control screen loop"""
        while self.running:
            self.handle_events()
            self.render()
        return

