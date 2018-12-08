from puzzle.day08 import *
import os


def test_should_sum_meta():
    assert sum_meta('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2') == 138


def test_should_solve_part1():
    input = open(os.path.join(os.path.dirname(__file__), 'day08_input.txt')).read()
    assert sum_meta(input) == 41555


def test_should_calculate_root_node_value():
    assert root_node_value('2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2') == 66


def test_should_solve_parts():
    input = open(os.path.join(os.path.dirname(__file__), 'day08_input.txt')).read()
    assert root_node_value(input) == 16653

