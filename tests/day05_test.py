from puzzle.day05 import *
import os


def test_should_react_example():
    example = 'dabAcCaCBAcCcaDA'
    assert react(example) == 'dabCBAcaDA'


def test_should_solve_part1():
    polymer = open(os.path.join(os.path.dirname(__file__), 'day05_input.txt')).read()
    assert units_remaining_after_reaction(polymer) == 11720


def test_should_solve_part2():
    polymer = open(os.path.join(os.path.dirname(__file__), 'day05_input.txt')).read()
    assert units_remaining_after_manipulation_and_reaction(polymer) == 4956


