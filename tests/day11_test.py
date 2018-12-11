from puzzle.day11 import *


def test_should_create_grid():
    grid = Grid(serial=20, size=10)
    assert grid.serial == 20
    assert grid.size == 10


def test_should_calculate_power_level_example_1():
    assert Grid(serial=8).power_level(3, 5) == 4


def test_should_calculate_power_level_example_2():
    assert Grid(serial=57).power_level(122, 79) == -5


def test_should_calculate_power_level_example_3():
    assert Grid(serial=39).power_level(217, 196) == 0


def test_should_calculate_power_level_example_4():
    assert Grid(serial=71).power_level(101, 153) == 4


def test_should_find_largest_total_power_area():
    grid = Grid(serial=18)
    assert grid.largest_total_power_area() == (33, 45)


def test_should_solve_part_1():
    grid = Grid(serial=9810)
    assert grid.largest_total_power_area() == (245, 14)


def test_should_find_largest_total_power_area_of_any_size():
    grid = Grid(serial=18)
    assert grid.largest_total_power_area_of_any_size() == (90, 269, 16)


def test_should_solve_part_2():
    grid = Grid(serial=9810)
    assert grid.largest_total_power_area_of_any_size() == (235, 206, 13)
