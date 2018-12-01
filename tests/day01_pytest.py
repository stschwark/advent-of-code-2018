from puzzle.day01 import *


def test_should_calculate_frequency():
    changes = ["+1", "-2", "+3", "+1"]
    assert frequency(changes) == 3


def test_should_solve_part1():
    changes = open("day01_input.txt", "r")
    assert frequency(changes.readlines()) == 538


def test_should_find_first_recurring_frequency_for_example_1():
    changes = ["+1", "-1"]
    assert recurring_frequency(changes) == 0


def test_should_find_first_recurring_frequency_for_example_2():
    changes = ["+3", "+3", "+4", "-2", "-4"]
    assert recurring_frequency(changes) == 10


def test_should_find_first_recurring_frequency_for_example_3():
    changes = ["-6", "+3", "+8", "+5", "-6"]
    assert recurring_frequency(changes) == 5


def test_should_find_first_recurring_frequency_for_example_4():
    changes = ["+7", "+7", "-2", "-7", "-4"]
    assert recurring_frequency(changes) == 14


def test_should_solve_part2():
    changes = open("day01_input.txt", "r")
    assert recurring_frequency(changes.readlines()) == 77271
