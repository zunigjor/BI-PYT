import pytest

from semestralka.src.classes import food
from semestralka.src.config import gameconfig as gc


def test_food_get_postition():
    t_food = food.Food()
    assert t_food.get_postion() == t_food.position


def test_food_init():
    t_food = food.Food()
    test_food_pos = t_food.get_postion()
    assert test_food_pos[0] >= 0
    assert test_food_pos[0] <= gc.SCREEN_WIDTH
    assert test_food_pos[1] >= 0
    assert test_food_pos[1] <= gc.SCREEN_HEIGHT


def test_food_random_position():
    t_food = food.Food()
    test_food_pos = t_food.get_postion()
    assert test_food_pos[0] >= 0
    assert test_food_pos[0] <= gc.SCREEN_WIDTH
    assert test_food_pos[1] >= 0
    assert test_food_pos[1] <= gc.SCREEN_HEIGHT

    for i in range(10000):
        t_food.random_position()
        test_food_pos = t_food.get_postion()
        assert test_food_pos[0] >= 0
        assert test_food_pos[0] <= gc.SCREEN_WIDTH
        assert test_food_pos[1] >= 0
        assert test_food_pos[1] <= gc.SCREEN_HEIGHT

