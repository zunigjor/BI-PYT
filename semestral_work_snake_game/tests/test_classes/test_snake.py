import pytest

import random

import pygame
import pygame.locals

from semestralka.src.classes import snake
from semestralka.src.config import gameconfig as gc


def test_snake_init():
    expected_direction = (0, 0)
    t_snake = snake.Snake()
    assert expected_direction == t_snake.direction


def test_snake_get_head():
    t_snake = snake.Snake()
    assert t_snake.get_head() == t_snake.positions[0]


def test_snake_get_tail():
    t_snake = snake.Snake()
    assert t_snake.get_tail() == t_snake.positions[-1]


def test_snake_turn():
    # Turn change test
    t_snake = snake.Snake()
    t_snake.turn(gc.UP)
    assert t_snake.direction == gc.UP
    # Cannot turn back into itself
    t_snake.length = 2
    t_snake.move()
    t_snake.turn(gc.DOWN)
    t_snake.move()
    assert t_snake.direction == gc.UP


def test_snake_move():
    t_snake = snake.Snake()
    t_snake.direction = gc.RIGHT

    current_pos = t_snake.get_head()
    x, y = t_snake.direction
    next_pos = ((current_pos[0] + (x * gc.SQUARE_SIZE)), (current_pos[1] + (y * gc.SQUARE_SIZE)))

    t_snake.move()

    assert t_snake.get_head() == next_pos


def test_snake_move_in_random_directions():
    t_snake = snake.Snake()
    moves = random.randint(50, 500)
    for i in range(moves):
        next_dir = random.choice([gc.UP, gc.DOWN, gc.LEFT, gc.RIGHT])
        t_snake.turn(next_dir)
        t_snake.move()
        for pos in t_snake.positions:
            assert pos[0] >= 0
            assert pos[0] <= gc.SCREEN_WIDTH
            assert pos[1] >= 0
            assert pos[1] <= gc.SCREEN_HEIGHT


def test_snake_reset():
    t_snake = snake.Snake()
    default_pos = t_snake.get_head()
    # move the snake somewhere else
    t_snake.turn(gc.UP)
    t_snake.move()
    t_snake.length += 1
    t_snake.move()
    t_snake.move()
    assert t_snake.get_head() != default_pos

    t_snake.reset()

    assert t_snake.get_head() == default_pos
    assert t_snake.length == 1


def test_snake_handle_input():
    t_snake = snake.Snake()
    test_event = pygame.event.Event(pygame.locals.KEYDOWN)
    test_event.key = pygame.K_w
    t_snake.handle_input(test_event)
    assert t_snake.direction == gc.UP
    test_event.key = pygame.K_s
    t_snake.handle_input(test_event)
    assert t_snake.direction == gc.DOWN
    test_event.key = pygame.K_a
    t_snake.handle_input(test_event)
    assert t_snake.direction == gc.LEFT
    test_event.key = pygame.K_d
    t_snake.handle_input(test_event)
    assert t_snake.direction == gc.RIGHT
