import pygame
import sys

from classes import main_game_menu


def main():
    """main"""
    pygame.init()
    pygame.display.set_caption("BI-PYT 2020 Snake Clone, made by zunigjor")

    snake_game = main_game_menu.MainGameMenu()
    snake_game.run()

    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
